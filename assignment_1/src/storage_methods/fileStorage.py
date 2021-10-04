
from .abstract_storage import Storage
import os
class FileStorage(Storage):
    def __init__(self, path_to_storage="storage"):
        if not os.path.exists(path_to_storage):
            raise ValueError("Storage folder does not exist")

        self.path_to_storage = path_to_storage

    def store(self, filename, content):
        with open(f"{self.path_to_storage}/{filename}", "wb+") as f:
            f.write(content)

    def retrieve(self, filename):
        with open(f"{self.path_to_storage}/{filename}","rb") as f:
            content = f.read()
        
        return content

    def remove(self, filename):
        os.remove(f"{self.path_to_storage}/{filename}")