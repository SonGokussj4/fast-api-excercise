from typing import Any, Dict, Optional, Union

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.rating import Rating
from app.schemas.rating import RatingCreate, RatingUpdate


class CRUDRating(CRUDBase[Rating, RatingCreate, RatingUpdate]):

    async def get_all(self, db: Session) -> Optional[Rating]:
        return db.query(Rating).all()

rating = CRUDRating(Rating)
