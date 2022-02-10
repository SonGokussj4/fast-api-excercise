from datetime import datetime
from typing import Optional, Sequence

from pydantic import BaseModel, EmailStr, HttpUrl
from sqlalchemy import JSON, DateTime, Boolean
from app.schemas.user import User
from app.schemas.movie import Movie

# from pydantic import BaseModel, validator
# from sqlalchemy.orm import Query

class RatingBase(BaseModel):
    Id: int
    Rating: int
    Date: datetime
    Computed: Optional[bool]
    LastUpdate: datetime
    UserId: int
    MovieId: int

    # UserId = Column(Integer, ForeignKey('User.Id'))
    # MovieId = Column(Integer, ForeignKey('Movie.Id'))

    # Pre-processing validator that evaluates lazy relationships before any other validation
    # NOTE: If high throughput/performance is a concern, you can/should probably apply
    #       this validator in a more targeted fashion instead of a wildcard in a base class.
    #       This approach is by no means slow, but adds a minor amount of overhead for every field
    # @validator("*", pre=True)
    # def evaluate_lazy_columns(cls, v):
    #     if isinstance(v, Query):
    #         return v.all()
    #     return v

    class Config:
        orm_mode = True

class RatingBaseWithUser(RatingBase):
    User: User

# Properties to receive via API on creation
class RatingCreate(RatingBase):
    ...


# Properties to receive via API on update
class RatingUpdate(RatingBase):
    ...


# Additional properties to return via API
class Rating(RatingBase):
    pass

class UserRating(RatingBase):
    MovieTitle: Optional[str]
    Username: Optional[str]
    pass


class RatingSearchResults(BaseModel):
    results: Sequence[RatingBaseWithUser]
    count: int


class UserRatings(BaseModel):
    results: Sequence[UserRating]
    count: int
