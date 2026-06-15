
from fastapi import FastAPI

from app.database.connection import engine
from app.models.movie import Movie

Movie.metadata.create_all(bind=engine)

app = FastAPI(
    title="CineMatch AI",
    description="An explainable hybrid movie recommendation system.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CineMatch AI 🎬"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CineMatch AI Backend"
    }