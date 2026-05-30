# create the vectorDB and ingest data into it. 
# later use the vectorDB to retrieve relevant information for the LLM to answer questions.

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import jsonlines
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data"
CHUNKS_FILE = BASE_DIR / "chunks.jsonl"
VECTORDB_DIR = BASE_DIR / "vectordb"

# Define the Markdown headers we want to split the document on
HEADERS_TO_SPLIT_ON = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

# Secondary chunker safety net: in case a section under a header is still massive
CHUNK_SIZE = 512
CHUNK_OVERLAP = 50

def ingest():
    # 1. Initialize our splitters
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS_TO_SPLIT_ON)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP
    )
    
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    all_chunks = []

    # 2. Recursively find all .md files
    for md_file in RAW_DIR.rglob("*.md"):
        print(f"Processing {md_file.name}...")
        
        # Extract metadata from file path
        vendor = md_file.stem.split("_")[0] 
        category = md_file.parent.name
        
        # Read the raw markdown text
        text = md_file.read_text(encoding="utf-8")

        # 3. Split by Markdown headers first
        md_header_splits = markdown_splitter.split_text(text)
        
        # 4. Apply the secondary character splitter to ensure chunks aren't too large
        final_chunks = text_splitter.split_documents(md_header_splits)

        for chunk in final_chunks:
            # The markdown splitter automatically creates metadata for the headers (e.g. {"Header 2": "Pricing"})
            # We merge our custom category and vendor metadata into it.
            merged_metadata = chunk.metadata.copy()
            merged_metadata.update({
                "source": md_file.name,
                "vendor": vendor,
                "category": category
            })
            
            all_chunks.append({
                "text": chunk.page_content,
                "metadata": merged_metadata
            })

    # 5. Save locally and to Chroma
    with jsonlines.open(CHUNKS_FILE, "w") as writer:
        writer.write_all(all_chunks)

    texts = [c["text"] for c in all_chunks]
    metas = [c["metadata"] for c in all_chunks]
    
    Chroma.from_texts(
        texts, 
        embedding, 
        metadatas=metas,
        persist_directory=str(VECTORDB_DIR)
    )

    print(f"Done — {len(all_chunks)} logically split chunks stored.")

if __name__ == "__main__":
    ingest()
