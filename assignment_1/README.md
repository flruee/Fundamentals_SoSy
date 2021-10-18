# FSS Assignment 1
### Members
Psarra Foteini  
Ben Murphy - 16-714-925
Florian Rüegsegger - 14-714-737  
## Setup
* Create venv via `python -m venv FSS_env`
* activate venv via `source FSS_env/bin/activate` (linux)
* install requirements via pip `pip install -r requirements.txt`

## Usage
Call main.py via terminal and add arguments:
* -s: Serializer, choices=[pickle]
* -m: Method, choices=[store, retrieve]
* filePath: path to a file

Example:  
`python main.py -s pickle -m store test.txt`, for pickling a file and storing it in a folder.  
`python main.py -s pickle -m retrieve test.txt`, for retrieving above file and storing it in your current directory.

## Structure
* src/serializers/: Contains serializer classes, implemented as defined in serializer_abstract.py
* src/storage_methods: Contains storage method classes, implemented as defined in abstract_storage.py
* src/storageHandler: class that is built with a storage method and a serializer. It can either serialize a File and store it or retrieve a file and deserialize it.