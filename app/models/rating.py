from sqlalchemy import Integer, String, Column, Boolean, Unicode, DateTime, JSON, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Rating(Base):

    __tablename__ = 'UserRating'
    __table_args__ = (UniqueConstraint('UserId', 'MovieId', name='_UserId_MovieId_uc'),)

    Id = Column(Integer, primary_key=True)
    Rating = Column(Integer, nullable=False)
    Date = Column(DateTime, nullable=True)
    Computed = Column(Boolean, nullable=True)
    LastUpdate = Column(DateTime, nullable=False)

    UserId = Column(Integer, ForeignKey('User.Id'))
    MovieId = Column(Integer, ForeignKey('Movie.Id'))

    User = relationship("User", back_populates="Ratings")  # , lazy="joined"
    Movie = relationship("Movie", back_populates="Ratings")
