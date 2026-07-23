from fastapi import FastAPI
from app.api.diseases import router as disease_router

app = FastAPI(
    title="Disease Gene Explorer",
    version="0.1.0"
)

app.include_router(disease_router)

@app.get("/")
def root():
    return {
        "message": "Disease Gene Explorer API is running!"
    }