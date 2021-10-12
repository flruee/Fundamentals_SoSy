#from . import Serializer
import json
class ProtonbuffSerializer():

    def serialize(self, content: str):
        return json.dumps(content)


if __name__ == "__main__":
    pr = ProtonbuffSerializer()
    with open("test_files/1mb.txt", "rb") as f:
        data = f.read()
    print(data)
    pr.serialize(data)