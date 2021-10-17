import csv
from os import read

from src.timer_methods.timer import ipfs_timer
from .serializer_abstract import Serializer

class CSVSerializer(Serializer):
    file_ending = ".csv"
    @ipfs_timer
    def serialize(self, content: str):
        content = str(content)
        #lines = content.split(sep="8")
        
        reader = csv.reader(content, delimiter='7')
        rows = []
        #serialized = ",".join([value for value in row] for row in list(reader)[0])
        serialized = ""
        for row in reader:
            serialized+="\t".join(value for value in row)
            serialized+="\n"
        serialized = bytes(serialized, "utf-8")
        print(serialized)
        return serialized  
        

    @ipfs_timer
    def deserialize(self, serialized_content):
        serialized_content = serialized_content.decode("utf-8").replace("\n", "")
        print(serialized_content)
        reader = csv.reader(serialized_content, delimiter="\t")
        row = []
        deserialized = ""
        for row in reader:
            print(row)
            deserialized+="7".join(value for value in row)
        print(deserialized)
        deserialized = bytes(deserialized,"utf-8")[2:-1]
          
        return deserialized

        return 1
        pass
        #return pickle.loads(serialized_content)
# Reading CSV content from a file import csv with open('/tmp/file.csv', newline='') as f: reader = csv.reader(f) for row in reader: print(row) 
# Writing CSV content to a file import csv with open('/temp/file.csv', 'w', newline='') as f: writer = csv.writer(f) writer.writerows(iterable) 