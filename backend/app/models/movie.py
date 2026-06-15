from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    year = Column(Integer)