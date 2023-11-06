from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    first_name: str = Field("Bill", min_length=3, max_length=12)
    email: EmailStr
    description: str


class ResponseUser(BaseModel):
    id: int = 1
    email: EmailStr

    class Config:
        orm_mode = True
