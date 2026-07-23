from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.diseases import router as disease_router
from app.api.genes import router as gene_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(disease_router)
app.include_router(gene_router)


@app.get("/")
def root():
    return {
        "message": "Disease Gene Explorer API is running!"
    }