import os
import pickle
import json
from src.serializers.serializer_abstract import Serializer
from src.storage_methods import Storage

class StorageHandler:
    def __init__(self, storer: Storage, serializer: Serializer, path_to_content="content.json"):

        if not os.path.exists(path_to_content):
            with open(path_to_content, "w+") as f:
                f.write("{}")


        self.path_to_content = path_to_content
        self.storer = storer
        self.serializer = serializer

    def store(self, file_path):
        file_name=file_path.split("/")[-1]
        with open(file_path, "rb") as f:
            file_str = f.read()

        serialized = self.serializer.serialize(file_str)
        file_name_stored = file_name + self.serializer.file_ending

        hash = self.storer.store(file_name_stored, serialized)
        self._add_content(file_name, hash)


    def _add_content(self,file_name: str, stored_name: str):
        with open(self.path_to_content,"r") as f:
            content = json.loads(f.read())
        
        content[file_name] = stored_name

        with open(self.path_to_content, "w") as f:
            f.write(json.dumps(content, indent=4,))


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