from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
from app.schemas.rating import Rating, RatingSearchResults

router = APIRouter()


@router.get("/", status_code=200, response_model=RatingSearchResults)
async def fetch_all_movies(*, db: Session = Depends(deps.get_db)) -> dict:
    """
    Fetch all Ratings
    """
    ratings = await crud.rating.get_all(db)
    return {
        "results": ratings,
        "count": len(ratings)
    }
