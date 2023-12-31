from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ResponseUser, UserModel, UserEmailModel
from src.repository import users as repository_users


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[ResponseUser])
async def get_users(db: Session = Depends(get_db)):
    users = await repository_users.get_users(db)
    return users


@router.get("/{user_id}", response_model=ResponseUser)
async def get_user(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    user = await repository_users.get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user


@router.post("/", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
async def create_user(body: UserModel, db: Session = Depends(get_db)):
    user = await repository_users.create_user(body, db)
    return user


@router.put("/{user_id}", response_model=ResponseUser)
async def update_user(
    body: UserModel, user_id: int = Path(ge=1), db: Session = Depends(get_db)
):
    user = await repository_users.update_user(body, user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user


@router.patch("/{user_id}", response_model=ResponseUser)
async def update_user_email(
    body: UserEmailModel, user_id: int = Path(ge=1), db: Session = Depends(get_db)
):
    user = await repository_users.update_user_email(body, user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_user(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    user = await repository_users.remove_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user


@router.get(
    "/search/",
    response_model=List[ResponseUser],
)
async def search_user(
    q: str = Query(description="Search by name, last name or email"),
    skip: int = 0,
    limit: int = Query(
        default=10,
        le=100,
        ge=10,
    ),
    db: Session = Depends(get_db),
):
    users = await repository_users.search_user(db, q, skip, limit)
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return users


@router.get("/birthdays/", response_model=List[ResponseUser])
async def birthday_users(
    days: int = Query(default=7, description="Enter the number of days"),
    skip: int = 0,
    limit: int = Query(
        default=10,
        le=100,
        ge=10,
    ),
    db: Session = Depends(get_db),
):
    birthday_users = await repository_users.birthdays_per_week(db, days, skip, limit)
    if birthday_users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return birthday_users
