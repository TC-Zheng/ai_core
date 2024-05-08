from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession


class RepositoryBase(ABC):
    def __init__(self) -> None:
        self.rollback_occurred: bool = False

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError("Each child class must implement this method")


class DBRepositoryBase(RepositoryBase):
    def __init__(self, async_session: AsyncSession) -> None:
        super().__init__()
        self.async_session = async_session

    def rollback(self) -> None:
        self.async_session.rollback()


class FileRepositoryBase(RepositoryBase):
    def __init__(self, file_path: str) -> None:
        super().__init__()
        self.file_path = file_path

    def rollback(self) -> None: ...
