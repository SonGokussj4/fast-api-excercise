from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
from app.schemas.rating import Rating, RatingSearchResults

router = APIRouter()


@router.get("/", status_code=200, response_model=RatingSearchResults)
async def fetch_all_user_ratings(*, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch all Ratings
    """
    ratings = await crud.rating.get_all(db)
    return {
        "results": ratings,
        "count": len(ratings)
    }

@router.get("/{user_id:int}/{movie_id:int}", status_code=200, response_model=Rating, summary="Fetch a Rating by UserID and MovieID")
async def fetch_rating_by_id(*, user_id: int, movie_id: int, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch a single user rating by UserId and MovieId
    """
    rating: Rating = await crud.rating.get_by_id(db, user_id=user_id, movie_id=movie_id)
    if not rating:
        raise HTTPException(status_code=404, detail="User not found")
    return rating

@router.post("/", status_code=200, response_model=Rating, summary="Add a Rating")
async def add_rating(*, rating: Rating, db: Session = Depends(deps.get_db)) -> dict:
    """
    Add a rating to DB
    """
    print("[ DEBUG] rating.add_rating()", rating)
    print("[ DEBUG] Adding rating...", rating)
    _rating = await crud.rating.add_rating(db, rating=rating)
    print(f'_rating: {_rating}')
    if not _rating:
        raise HTTPException(status_code=404, detail=f"Rating for movie '{rating.MovieId}' and user '{rating.UserId}' couldn't be added")
    return _rating
