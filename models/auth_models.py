from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List

ALLOWED_ROLES = {"student", "admin"}

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    roles: List[str]

class TokenData(BaseModel):
    email: EmailStr | None = None
    roles: List[str] = []

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class RegisterUser(BaseModel):
    name: str | None = None
    email: EmailStr
    contactnumber: str | None = None
    password: str
    roles: List[str] = ["student"]


class User(BaseModel):
    userId: str
    name: str | None = None
    email: EmailStr
    contactnumber: str | None = None
    roles: List[str]

class UserInDB(User):
    hashed_password: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr
    contactnumber: str | None = None

class EmailOnlyRequest(BaseModel):
    email: EmailStr