from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ResponseUser, UserModel
from src.repository import users as repository_users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[ResponseUser])
async def get_users(db: Session = Depends(get_db)):
    users = await repository_users.get_users(db)
    return users


@router.get("/{user_id}", response_model=ResponseUser)
async def get_user(user_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    user = await repository_users.get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user


@router.post("/", response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
async def create_owner(body: UserModel, db: Session = Depends(get_db)):
    user = await repository_users.create_user(body, db)
    return user


@router.put("/{user_id}", response_model=ResponseUser)
async def update_user(
    body: UserModel, user_id: int = Path(1, ge=1), db: Session = Depends(get_db)
):
    user = await repository_users.update_user(body, user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_user(user_id: int = Path(1, ge=1), db: Session = Depends(get_db)):
    user = await repository_users.remove_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user
