from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Dict, Any, Union

T = TypeVar("T")  # Generic type variable for entity types


class RepositoryBase(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def read_all(self) -> List[T]:
        pass

    @abstractmethod
    def read(self, criteria: Dict[str, Any]) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, entity: T) -> T:
        pass
