from abc import ABC, abstractmethod

from domain.user.model import User


class UserStorageI(ABC):

    @abstractmethod
    def get_one(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_all(self, limit: int, offset: int) -> list[User]:
        pass

    @abstractmethod
    def create(self, user: User) -> int:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass
