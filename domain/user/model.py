from sqlalchemy import Column, Integer, String, Table
from ..mapper import mapper_registry, metadata


class User:
    id: int
    name: str
    age: int


user_table = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer)
)

mapper_registry.map_imperatively(User, user_table)
