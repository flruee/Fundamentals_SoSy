from ipfshttpclient.client import connect
from .abstract_storage import Storage
import io
import ipfshttpclient
import requests
#from storage_methods.abstract_storage import Storage


class IPFSStorage():
    def __init__(self, ip: str="127.0.0.1", port: int=5001):
        self.ip = ip
        self.port = port
        #self.client = ipfsApi.Client()
        self.client = ipfshttpclient.Client()

    def store(self, filename,content):
        print(filename)
        print(content)
        #multihash = self.client.add_bytes(content)
        multihash = self.client.block.put(io.BytesIO(content))
        
        return multihash["Key"]

    def retrieve(self,multihash):
        """
        hash = multihash["Hash"]

        print(r.text)
        print(type(r.text))
        for i in r.text:
            print(i,end="")
        content = r.text
        #print(content)
        self.client = ipfsApi.Client(self.ip,self.port)
        """
        print(multihash)
        x = self.client.block.get(multihash)
        print(x)
        return x

    def remove(self,filename):
        return



if __name__ == "__main__":
    ipfs_storage = IPFSStorage()
    hash = ipfs_storage.store("test.txt")
    ipfs_storage.retrieve(hash)
    #client = ipfsApi.Client("127.0.0.1", 5001)
    #res = client.add("test.txt")
    #print(res)