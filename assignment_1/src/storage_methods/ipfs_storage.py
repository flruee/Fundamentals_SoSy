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
        self.client = ipfshttpclient.Client()
        #self.client = ipfshttpclient.connect()
        print(self.client.id())

    def store(self, filename,content):
        #multihash = self.client.block.put(io.BytesIO(content))
        multihash = self.client.add(io.BytesIO(content))

        print(multihash)
        #return multihash["Key"]
        return multihash["Hash"]
    def retrieve(self,multihash):
        #return self.client.block.get(multihash)
        return self.client.get(multihash)
    def remove(self,filename):
        return



if __name__ == "__main__":
    ipfs_storage = IPFSStorage()
    hash = ipfs_storage.store("test.txt")
    ipfs_storage.retrieve(hash)
    #client = ipfsApi.Client("127.0.0.1", 5001)
    #res = client.add("test.txt")
