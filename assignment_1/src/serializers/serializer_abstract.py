from abc import ABC, abstractmethod

class Serializer(ABC):

    file_ending: str
    @abstractmethod
    def serialize(self, content: str):
        pass

    @abstractmethod
    def deserialize(self, serialized_content):
        pass