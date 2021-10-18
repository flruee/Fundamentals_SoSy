
import sys
import argparse
from src.storageHandler import StorageHandler
from src.storage_methods import FileStorage
from src.serializers import PickleSerializer, CSVSerializer
from src.storage_methods import IPFSStorage
from src.http_functions import http_runs

def setup_parser():
    parser = argparse.ArgumentParser(description="Serialize and store files or deserialize and retrieve files")
    parser.add_argument("--filepath", required=False, help="filepath for the file you want to process")
    parser.add_argument("-s", type=str, required=False, choices=["pickle", "csv"], help="Serializer method. Valid values are: pickle")
    parser.add_argument("-m",type=str, required=False, choices=["store", "retrieve", "http"], help="if you want to store the file")
    return parser

def build_storage():
    return IPFSStorage()

def build_serializer(id: str):
    if id=="pickle":
        return PickleSerializer()
    elif id=="csv":
        return CSVSerializer()
    else:
        raise ValueError("{id} is an invalid serializer method")

if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args(sys.argv[1:])
    
    if(args.m == "http"):
        http_runs()
    else:    
        file = args.filepath
        file_storer = build_storage()
        serializer = build_serializer(args.s)
        sh = StorageHandler(file_storer,serializer)

        if args.m == "store":
            print(f"storing {file} with serializer {args.s}")
            sh.store(file)
        elif args.m == "retrieve":
            print(f"retrieving {file} with with deserializer {args.s}")
            sh.retrieve(file)
        else:
            raise ValueError(f"{args.m} is invalid")