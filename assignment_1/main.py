
import sys
import argparse
from src.storageHandler import StorageHandler
from src.storage_methods import FileStorage
from src.serializers import PickleSerializer

def setup_parser():
    parser = argparse.ArgumentParser(description="Serialize and store files or deserialize and retrieve files")
    parser.add_argument("filepath", help="filepath for the file you want to process")
    parser.add_argument("-st", type=str, required=True, choices=["file"], help="Storage method. Valid values are: file")
    parser.add_argument("-se", type=str, required=True,choices=["pickle"], help="Serializer method. Valid values are: pickle")
    parser.add_argument("-m",type=str, required=True, choices=["store", "retrieve"], help="if you want to store the file")
    return parser

def build_storage(id: str):
    if id=="file":
        return FileStorage()
    else:
        raise ValueError("{id} is an invalid storage method")

def build_serializer(id: str):
    if id=="pickle":
        return PickleSerializer()
    else:
        raise ValueError("{id} is an invalid serializer method")

if __name__ == "__main__":

    parser = setup_parser()
    args = parser.parse_args(sys.argv[1:])
    
    file = args.filepath
    file_storer = build_storage(args.st)
    serializer = build_serializer(args.se)
    sh = StorageHandler(file_storer,serializer)

    if args.m == "store":
        print(f"storing {file} in {args.st} with serializer {args.se}")
        sh.store(file)
    elif args.m == "retrieve":
        print(f"retrieving {file} from {args.st} with deserializer {args.se}")
        sh.retrieve(file)
    else:
        raise ValueError(f"{args.m} is invalid")