from datetime import date

from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=30)
    email: EmailStr
    phone_number: str = Field(max_length=25)
    born_date: date
    description: str = Field(max_length=250)


class ResponseUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    born_date: date
    description: str | None = None

    class Config:
        orm_mode = True


class UserEmailModel(BaseModel):
    email: EmailStr
