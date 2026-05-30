from fastapi import FastAPI

from app.routes import normalise, upload


app = FastAPI(
    title="Vendor Decision API",
    description="Normalises vendor quotations and ranks them against company metrics.",
    version="0.1.0",
)

app.include_router(upload.router)
app.include_router(normalise.router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
