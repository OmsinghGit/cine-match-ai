
from fastapi import FastAPI

from app.database.connection import engine
from app.models.movie import Movie

from sqlalchemy.orm import Session
from app.database.connection import SessionLocal

from app.services.recommendation import recommend_movies

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

@app.get("/movies")
def get_movies():
    db: Session = SessionLocal()

    movies = db.query(Movie).limit(10).all()

    result = []

    for movie in movies:
        result.append({
            "id": movie.id,
            "title": movie.title,
            "genre": movie.genre
        })

    db.close()

    return result

@app.get("/recommend")
def recommend(movie: str):
    recommendations = recommend_movies(movie)

    return {
        "movie": movie,
        "recommendations": recommendations
    }