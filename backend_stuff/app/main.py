from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import catalog, metrics, normalise, requirements, upload, evaluation
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="Vendor Decision API",
    description="Normalises vendor quotations and ranks them against company metrics.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(normalise.router)
app.include_router(metrics.router)
app.include_router(requirements.router)
app.include_router(catalog.router)
app.include_router(evaluation.router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
