from sqlalchemy import Column, Integer, String, Date, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(25), nullable=False, index=True)
    last_name = Column(String(30), nullable=False, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String(25), nullable=False)
    born_date = Column(Date, nullable=False)
    description = Column(String(250))
    created_at = Column("created_at", DateTime, default=func.now())
