
from src.timer_methods.timer import ipfs_timer
from .serializer_abstract import Serializer


class CSVSerializer(Serializer):

    def __init__(self, seperator=b","):
        self.seperator = seperator

    file_ending = ".csv"
    @ipfs_timer
    def serialize(self, file_path: str):

        with open(file_path, "rb") as f:
            data = f.read()

        data = data.replace(self.seperator, b"thisIsASeperator")
        return data
  
        

    @ipfs_timer
    def deserialize(self, serialized_content):
        deserialized = serialized_content.replace(b"thisIsASeperator", b",")
          
        return deserialized
