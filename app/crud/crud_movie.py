from typing import Any, Dict, Optional, Union

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

    # async def get_by_id(self, db: Session, *, Movie_id: int) -> Optional[Movie]:
    #     return db.query(Movie).filter(Movie.Id == Movie_id).first()

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
