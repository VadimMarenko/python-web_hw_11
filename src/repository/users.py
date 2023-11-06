from sqlalchemy.orm import Session

from src.database.models import Users
from src.schemas import UserModel


async def get_users(db: Session):
    users = db.query(Users).all()
    return users


async def get_user(user_id: int, db: Session):
    user = db.query(Users).filter_by(id=user_id).first()
    return user


async def create_user(body: UserModel, db: Session):
    user = Users(**body.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def update_user_email(body: UserModel, user_id: int, db: Session):
    user = db.query(Users).filter_by(id=user_id).first()
    if user:
        user.email = body.email
        db.commit()
    return user


async def remove_user(user_id: int, db: Session):
    user = db.query(Users).filter_by(id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
