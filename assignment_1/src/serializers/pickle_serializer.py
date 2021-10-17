import pickle

from src.timer_methods.timer import ipfs_timer

from .serializer_abstract import Serializer
class PickleSerializer(Serializer):

    @ipfs_timer
    def serialize(self, file_path: str):
        with open(file_path, "rb") as f:
            file_str = f.read()
        serialized = pickle.dumps(file_str)
        return serialized
    @ipfs_timer
    def deserialize(self, serialized_content):
        return pickle.loads(serialized_content)
