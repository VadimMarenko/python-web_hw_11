from datetime import date

from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    first_name: str = Field("Bill")
    last_name: str = Field("Jhonson")
    email: EmailStr = Field("user@example.com")
    phone_number: str = Field("+380 99 99 99 999")
    born_date: date = date(2000, 1, 1)
    description: str = Field("Customer")


class ResponseUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    born_date: date
    description: str

    class Config:
        orm_mode = True
