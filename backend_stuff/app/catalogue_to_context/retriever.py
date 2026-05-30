from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path

VECTORDB_DIR = Path(__file__).resolve().parent / "vectordb"
_db = None

def get_vendor_context(product: str, metrics: list[str], vendors: list[str] = None, category: str = None, k: int = 5) -> dict:
    db = _get_db()

    # Build query from product + metrics
    query = f"{product} {' '.join(metrics)}"

    filters = []
    if vendors:
        filters.append({"vendor": {"$in": vendors}})
    if category:
        filters.append({"category": category})
        
    # Chroma expects None if there are no filters
    if not filters:
        where = None
    elif len(filters) == 1:
        where = filters[0]
    else:
        where = {"$and": filters}

    results = db.similarity_search(query, k=k, filter=where)

    # Group results by vendor
    vendor_context = {}
    for r in results:
        vendor = r.metadata["vendor"]
        if vendor not in vendor_context:
            vendor_context[vendor] = []
        vendor_context[vendor].append(r.page_content)

    # Flatten each vendor's chunks into one string
    return {v: "\n\n".join(chunks) for v, chunks in vendor_context.items()}


def _get_db():
    global _db
    if _db is None:
        embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        _db = Chroma(
            persist_directory=str(VECTORDB_DIR),
            embedding_function=embedding,
        )
    return _db
