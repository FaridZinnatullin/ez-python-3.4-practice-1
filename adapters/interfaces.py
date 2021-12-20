from abc import ABC, abstractmethod
from typing import List

from domain.user.dto import *
from domain.user.model import User


class UserServiceI(ABC):
    @abstractmethod
    def get_users(self, limit: int, offset: int) -> List[User]: pass

    @abstractmethod
    def get_user(self, user_id) -> User: pass

    @abstractmethod
    def create_user(self, user: CreateUserDTO) -> int: pass

    @abstractmethod
    def delete_user(self, user_id) -> None: pass

    @abstractmethod
    def update_user(self, user: UpdateUserDTO) -> None: pass

    @abstractmethod
    def partially_update(self, user: PartiallyUpdateUserDTO) -> None: pass
