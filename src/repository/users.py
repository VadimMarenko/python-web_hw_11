from sqlalchemy.orm import Session

from src.database.models import Users
from src.schemas import UserModel, UserEmailModel


async def get_users(db: Session):
    users = db.query(Users).all()
    return users


async def get_user(user_id: int, db: Session):
    user = db.query(Users).filter_by(id=user_id).first()
    return user


async def get_user_by_name(user_name: str, db: Session):
    users = db.query(Users).filter_by(first_name=user_name).all()
    return users


async def get_user_by_surname(user_surname: str, db: Session):
    users = db.query(Users).filter_by(last_name=user_surname).all()
    return users


async def get_user_by_email(user_email: str, db: Session):
    user = db.query(Users).filter_by(email=user_email).first()
    return user


async def create_user(body: UserModel, db: Session):
    user = Users(**body.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def update_user(body: UserModel, user_id: int, db: Session):
    user = db.query(Users).filter_by(id=user_id).first()
    if user:
        user.first_name = body.first_name
        user.last_name = body.last_name
        user.email = body.email
        user.phone_number = body.phone_number
        user.born_date = body.born_date
        user.description = body.description
        db.commit()
    return user


async def update_user_email(body: UserEmailModel, user_id: int, db: Session):
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
