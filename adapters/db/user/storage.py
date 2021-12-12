from typing import List

from domain.user.exceptions import UserNotFoundException
from domain.user.model import User
from domain.user.storage import UserStorageI
from domain.user.dto import UpdateUserDTO, CreateUserDTO
from ..db_init import Session


class UserStorage(UserStorageI):

    def create(self, user: CreateUserDTO) -> int:
        with Session() as session:
            new_user = User(name=user.name, age=user.age)
            session.add(new_user)
            session.flush()
            user_id = new_user.id
            session.commit()
        return user_id

    def update(self, user: UpdateUserDTO) -> None:
        with Session() as session:
            user_query = session.query(User).filter_by(id=user.id).one_or_none()
            if not user_query:
                raise UserNotFoundException(message="user not found")
            user_query.name = user.name
            user_query.age = user.age
            session.flush()
            session.commit()
        return user_query

    def delete(self, user_id: int) -> None:
        with Session() as session:
            user = session.query(User).filter(User.id == user_id).one_or_none()
            if not user:
                raise UserNotFoundException(message="user not found")
            session.delete(user)
            session.commit()

    def get_one(self, user_id: str) -> User:
        with Session() as session:
            user = session.query(User).filter(User.id == user_id).one_or_none()
            
        if not user:
            raise UserNotFoundException(message="user not found")
        
        return user

    def get_all(self, limit: int, offset: int) -> List[User]:
        with Session() as session:
            users = session.query(User).offset(offset).limit(limit).all()
        return users
