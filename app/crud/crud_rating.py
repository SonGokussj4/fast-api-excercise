from typing import Any, Dict, Optional, Union
from fastapi import HTTPException

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.rating import Rating
from app.schemas.rating import RatingCreate, RatingUpdate


class CRUDRating(CRUDBase[Rating, RatingCreate, RatingUpdate]):

    async def get_all(self, db: Session) -> Optional[Rating]:
        return db.query(Rating).all()

    async def get_by_id(self, db: Session, *, user_id: int, movie_id) -> Optional[Rating]:
        rating: Rating = db.query(Rating).filter(Rating.UserId == user_id).filter(Rating.MovieId == movie_id).first()
        # if not rating:
        #     raise HTTPException(status_code=404, detail="Rating not found")
        return rating

    async def patch_ratings_by_id(self, db: Session, *, user_id: int, movie_id: int, body: Rating) -> Optional[Rating]:
        print(f"[ PATCH ] crud_user.patch_ratings_by_id(user_id={user_id}, movie_id={movie_id}, body={body}):")
        db_rating: Rating = db.query(Rating).filter(Rating.MovieId == movie_id).filter(Rating.UserId == user_id).first()
        if not db_rating:
            raise HTTPException(status_code=404, detail="Rating not found")

        db_rating.Rating = body.get("Rating")
        db_rating.Computed = body.get("Computed")
        db_rating.LastUpdate = body.get("LastUpdate")
        db_rating.Date = body.get("Date")

        db.commit()
        return db_rating

    async def add_rating(self, db: Session, *, rating: Rating) -> Optional[Rating]:
        print("[ DEBUG} crud_rating.add_rating()")
        db_rating = await self.get_by_id(db, user_id=rating.UserId, movie_id=rating.MovieId)
        print(f'[ DEBUG ] crud_rating.db_rating: {db_rating}')
        if db_rating:
            raise HTTPException(status_code=400, detail="Rating already exists")

        _rating = Rating(
            Rating=rating.Rating,
            Date=rating.Date,
            Computed=rating.Computed,
            LastUpdate=rating.LastUpdate,
            UserId=rating.UserId,
            MovieId=rating.MovieId,
        )
        db.add(_rating)
        db.commit()
        db.refresh(_rating)
        return _rating

    # async def add_user_ratings(self, db: Session, *, _rating: Rating) -> Optional[Movie]:
    #     db_rating = await self.get_all(db, movie_id=movie.Id)
    #     if db_movie:
    #         raise HTTPException(status_code=400, detail="Movie already exists")

    #     new_movie = Movie(
    #         Id=movie.Id,
    #         Url=movie.Url,
    #         Title=movie.Title,
    #         Type=movie.Type,
    #         Year=movie.Year,
    #         Genres=movie.Genres,
    #         GenresJson=json.loads(movie.Genres),
    #         FanclubCount=movie.FanclubCount,
    #         Country=movie.Country,
    #         Duration=movie.Duration,
    #         Rating=movie.Rating,
    #         RatingCount=movie.RatingCount,
    #         PosterUrl = movie.PosterUrl,
    #         LastUpdate=movie.LastUpdate,
    #         parentid=movie.parentid,
    #         SeasonId=movie.SeasonId,
    #         EpisodesCount=movie.EpisodesCount,
    #         SeasonsCount=movie.SeasonsCount,
    #     )
    #     db.add(new_movie)
    #     db.commit()
    #     db.refresh(new_movie)
    #     return new_movie

rating = CRUDRating(Rating)
