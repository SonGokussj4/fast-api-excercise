import json
from typing import Any, Dict, Optional, Union
from fastapi import HTTPException

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate


class CRUDMovie(CRUDBase[Movie, MovieCreate, MovieUpdate]):
    # def get_by_email(self, db: Session, *, email: str) -> Optional[Movie]:
    #     return db.query(Movie).filter(Movie.email == email).first()

    async def get_all(self, db: Session) -> Optional[Movie]:
        return db.query(Movie).all()

    async def get_by_id(self, db: Session, movie_id: int) -> Optional[Movie]:
        return db.query(Movie).filter(Movie.Id == movie_id).first()

    async def add_movie(self, db: Session, *, movie: Movie) -> Optional[Movie]:
        db_movie = await self.get_by_id(db, movie_id=movie.Id)
        if db_movie:
            raise HTTPException(status_code=400, detail="Movie already exists")

        new_movie = Movie(
            Id=movie.Id,
            Url=movie.Url,
            Title=movie.Title,
            Type=movie.Type,
            Year=movie.Year,
            Genres=movie.Genres,
            GenresJson=json.loads(movie.Genres),
            FanclubCount=movie.FanclubCount,
            Country=movie.Country,
            Duration=movie.Duration,
            Rating=movie.Rating,
            RatingCount=movie.RatingCount,
            PosterUrl = movie.PosterUrl,
            LastUpdate=movie.LastUpdate,
            parentid=movie.parentid,
            SeasonId=movie.SeasonId,
            EpisodesCount=movie.EpisodesCount,
            SeasonsCount=movie.SeasonsCount,
        )
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie

    # async def get_by_Moviename(self, db: Session, *, Moviename: str) -> Optional[Movie]:
    #     return db.query(Movie).filter(func.lower(Movie.Moviename) == func.lower(Moviename)).first()

    # async def get_ratings_by_Moviename(self, db: Session, *, Moviename: str) -> Optional[Movie]:
    #     return db.query(Movie).filter(func.lower(Movie.Moviename) == func.lower(username)).first()

    # def update(
    #     self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    # ) -> User:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)

    #     return super().update(db, db_obj=db_obj, obj_in=update_data)

    # def is_superuser(self, user: User) -> bool:
    #     return user.is_superuser


movie = CRUDMovie(Movie)
