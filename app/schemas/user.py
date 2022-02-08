from typing import Optional, Sequence

from pydantic import BaseModel, EmailStr, HttpUrl, constr


class UserBase(BaseModel):
    Id: int
    Username: constr(max_length=50)
    Realname: Optional[str] = None
    Url: str = None
    AvatarUrl: Optional[str] = None

    class Config:
        orm_mode = True

# Properties to receive via API on creation
class UserCreate(UserBase):
    ...


# Properties to receive via API on update
class UserUpdate(UserBase):
    ...


# Additional properties to return via API
class User(UserBase):
    pass


class UserSearchResults(BaseModel):
    results: Sequence[User]
    count: int
