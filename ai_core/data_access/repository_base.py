from abc import ABC, abstractmethod

class RepositoryBase(ABC):
    def __init__(self):
        self.rollback_occurred = False
    @abstractmethod
    def rollback(self):
        raise NotImplementedError("Each child class must implement this method")

class DBRepositoryBase(RepositoryBase):
    def __init__(self, async_session):
        super().__init__()
        self.async_session  = async_session 
    def rollback(self):
        self.rollback_occurred = True
        self.async_session .rollback()
        
class FileRepositoryBase(RepositoryBase):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
    def rollback(self):
        self.rollback_occurred = True
        
