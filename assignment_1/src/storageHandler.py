import os
import pickle
import json
from src.serializers.serializer_abstract import Serializer
from src.storage_methods import Storage
from src.timer_methods.timer import ipfs_timer

class StorageHandler:
    def __init__(self, storer: Storage, serializer: Serializer, path_to_content="content.json"):

        if not os.path.exists(path_to_content):
            with open(path_to_content, "w+") as f:
                f.write("{}")


        self.path_to_content = path_to_content
        self.storer = storer
        self.serializer = serializer

    @ipfs_timer
    def store(self, file_path):

        serialized = self.serializer.serialize(file_path)

        hash = self.storer.store(file_path, serialized)
        self._add_content(file_path, hash)
        print(hash)

    def _add_content(self,file_name: str, stored_name: str):
        with open(self.path_to_content,"r") as f:
            content = json.loads(f.read())
        
        content[file_name] = stored_name

        with open(self.path_to_content, "w") as f:
            f.write(json.dumps(content, indent=4,))

    @ipfs_timer
    def retrieve(self, file_name: str):
        stored_name = self._get_content(file_name)


        self.storer.retrieve(stored_name)
        with open(stored_name,"rb") as f:
            serialized = f.read()
        
        file_content = self.serializer.deserialize(serialized)
        with open(stored_name, "wb+") as f:
            f.write(file_content)

        #self.storer.remove(stored_name)
        #self._remove_content(file_name)


    def _get_content(self,file_name: str) -> str:
        with open(self.path_to_content, "r") as f:
            content = json.loads(f.read())

        if not file_name in content.keys():
            raise ValueError("File is not stored")
        else:
            return content[file_name]


    def _remove_content(self, file_name):
        with open(self.path_to_content, "r") as f:
            content = json.loads(f.read())

        del content[file_name]

        with open(self.path_to_content, "w") as f:
            f.write(json.dumps(content,indent=4))