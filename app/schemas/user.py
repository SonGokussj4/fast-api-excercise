from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl


class UserBase(BaseModel):
    Username: str
    Realname: Optional[str] = None
    Url: Optional[str] = None
    AvatarUrl: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    ...


# Properties to receive via API on update
class UserUpdate(UserBase):
    ...


class UserInDBBase(UserBase):
    Id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass
