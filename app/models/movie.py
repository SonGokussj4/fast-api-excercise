from sqlalchemy import Integer, String, Column, Boolean, Unicode, DateTime, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Movie(Base):
    Id = Column(Integer, primary_key=True)
    Url = Column(Unicode(255), unique=True, nullable=False)
    Title = Column(Unicode(255), unique=False, nullable=True)
    Type = Column(Unicode(32), unique=False, nullable=True)
    Year = Column(Unicode(16), unique=False, nullable=True)
    Duration = Column(Unicode(128), unique=False, nullable=True)
    Country = Column(Unicode(64), unique=False, nullable=True)
    Rating = Column(Integer, unique=False, nullable=True)
    RatingCount = Column(Integer, unique=False, nullable=True)
    FanclubCount = Column(Integer, unique=False, nullable=True)
    SeasonsCount = Column(Integer, unique=False, nullable=True)
    EpisodesCount = Column(Integer, unique=False, nullable=True)
    PosterUrl = Column(Unicode(255), unique=False, nullable=True)
    SeriesId = Column(Integer, unique=False, nullable=True)
    SeasonId = Column(Integer, unique=False, nullable=True)
    LastUpdate = Column(DateTime, unique=False, nullable=False)
    GenresJson = Column(JSON)
    ChildrenJson = Column(JSON)

    # Many-to-many
    # Genres = relationship('Genre', secondary=movie_genre, backref='Movies')

    # UserRatings = relationship(
    #     'UserRating',
    #     backref="Users"
    # )

    # # Many-to-many
    # Movies = relationship('Movie', secondary=user_movie, backref='Users')

    # @property
    # def serialize(self):
    #     """Return object data in easily serializable format"""
    #     return {
    #         "Id": self.Id,
    #         "Url": self.Url,
    #         "Username": self.Username,
    #         "Realname": self.Realname,
    #         "AvatarUrl": self.AvatarUrl
    #     }
