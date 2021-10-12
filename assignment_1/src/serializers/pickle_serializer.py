import pickle

from src.timer_methods.timer import ipfs_timer

from .serializer_abstract import Serializer
class PickleSerializer(Serializer):

    file_ending = ".pickle"
    @ipfs_timer
    def serialize(self, content: str):
        serialized = pickle.dumps(content)
        return serialized
    @ipfs_timer
    def deserialize(self, serialized_content):
        return pickle.loads(serialized_content)
