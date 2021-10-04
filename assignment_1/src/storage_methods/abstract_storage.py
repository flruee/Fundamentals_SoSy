from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def store(self, filename: str, content):
        pass
    
    @abstractmethod
    def retrieve(self, filename) -> str:
        pass
    
    @abstractmethod
    def remove(self, filename):
        pass