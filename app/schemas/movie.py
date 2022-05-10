from datetime import datetime
from typing import Optional, Sequence

from pydantic import BaseModel, EmailStr, HttpUrl
from sqlalchemy import JSON, DateTime


class MovieBase(BaseModel):
    Url: str = None
    Title: Optional[str] = None
    Type: Optional[str] = None
    Year: Optional[str] = None
    Duration: Optional[str] = None
    Country: Optional[str] = None
    Rating: Optional[int] = None
    RatingCount: Optional[int] = None
    FanclubCount: Optional[int] = None
    SeasonsCount: Optional[int] = None
    EpisodesCount: Optional[int] = None
    PosterUrl: Optional[str] = None
    SeriesId: Optional[int] = None
    SeasonId: Optional[int] = None
    LastUpdate: datetime
    GenresJson = JSON
    ChildrenJson = JSON
    Genres: Optional[str] = None


# Properties to receive via API on creation
class MovieCreate(MovieBase):
    ...


# Properties to receive via API on update
class MovieUpdate(MovieBase):
    ...


class MovieInDBBase(MovieBase):
    Id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class Movie(MovieInDBBase):
    pass


class MovieSearchResults(BaseModel):
    results: Sequence[Movie]
    count: int
