from typing import Any, Dict, Optional, Union

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.models.rating import Rating
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    # def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
    #     return db.query(User).filter(User.email == email).first()

    async def get_all(self, db: Session) -> Optional[User]:
        return db.query(User).all()

    async def get_by_id(self, db: Session, *, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.Id == user_id).first()

    async def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(func.lower(User.Username) == func.lower(username)).first()

    async def get_ratings_by_username(self, db: Session, *, username: str) -> Optional[User]:
        # user = db.query(User).filter(func.lower(User.Username) == func.lower(username)).first()
        # return db.query(Rating).filter(user.Id == Rating.UserId).all()
        return db.query(Rating).join(User).filter(func.lower(User.Username) == func.lower(username)).all()

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


user = CRUDUser(User)
