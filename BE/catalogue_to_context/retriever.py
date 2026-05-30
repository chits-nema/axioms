from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path

VECTORDB_DIR = Path("catalogue_to_context/vectordb")
_db = None

def get_vendor_context(product: str, metrics: list[str], vendors: list[str] = None, category: str = None, k: int = 5) -> dict:
    # ... [keep your setup] ...

    # Build query from product + metrics
    query = f"{product} {' '.join(metrics)}"

    # CHANGE 4: Build a dynamic 'where' filter combining vendor and category
    where = {}
    if vendors:
        where["vendor"] = {"$in": vendors}
    if category:
        where["category"] = category
        
    # Chroma expects None if there are no filters
    if not where:
        where = None

    results = _db.similarity_search(query, k=k, filter=where)

    # Group results by vendor
    vendor_context = {}
    for r in results:
        vendor = r.metadata["vendor"]
        if vendor not in vendor_context:
            vendor_context[vendor] = []
        vendor_context[vendor].append(r.page_content)

    # Flatten each vendor's chunks into one string
    return {v: "\n\n".join(chunks) for v, chunks in vendor_context.items()}