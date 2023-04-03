from config.database import Base

from sqlalchemy import Column, Integer, String, Float

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    overview = Column(String)
    year = Column(String)
    rating = Column(Float)
    category = Column(String)

    def __init__(self, title: str, overview: str, year: str, rating: float, category: str):
        self.title = title
        self.overview = overview
        self.year = year
        self.rating = rating
        self.category = category

    def __repr__(self):
        return f"Movie(title={self.title}, overview={self.overview}, year={self.year}, rating={self.rating}, category={self.category})"

    def __str__(self):
        return self.__repr__()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "overview": self.overview,
            "year": self.year,
            "rating": self.rating,
            "category": self.category
        }