from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
        
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)
    age: int = Column(Integer)
