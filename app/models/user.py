from sqlalchemy import Integer, String, Column, Boolean, Unicode
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    # id = Column(Integer, primary_key=True, index=True)
    # first_name = Column(String(256), nullable=True)
    # surname = Column(String(256), nullable=True)
    # email = Column(String, index=True, nullable=False)
    # is_superuser = Column(Boolean, default=False)
    # recipes = relationship(
    #     "Recipe",
    #     cascade="all,delete-orphan",
    #     back_populates="submitter",
    #     uselist=True,
    # )

    Id = Column(Integer, unique=True, primary_key=True)
    Url = Column(Unicode(255), unique=True, nullable=False)
    Username = Column(Unicode(50), unique=True, nullable=False)
    Realname = Column(Unicode(50), unique=False, nullable=True)
    AvatarUrl = Column(Unicode(255), unique=True, nullable=True)
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
