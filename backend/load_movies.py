import pandas as pd
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models.movie import Movie

MOVIES_PATH = "../datasets/tmdb_5000_movies.csv"

df = pd.read_csv(MOVIES_PATH)

db: Session = SessionLocal()

count = 0

for _, row in df.head(100).iterrows():
    movie = Movie(
        title=row["title"],
        genre=str(row["genres"]),
        year=None
    )

    db.add(movie)
    count += 1

db.commit()
db.close()

print(f"✅ {count} movies inserted successfully!")