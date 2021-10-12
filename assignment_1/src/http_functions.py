import requests
from src.timer_methods import timer

@timer.http_timer
def http_run(id, url:str):
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.text[:5])  
    
def http_runs():
    files = {
        "1" :  "https://filesender.switch.ch/filesender2/download.php?token=6de159f9-55ba-4661-9329-2cca0f4c9e67&files_ids=26095",
        "100" :  "https://filesender.switch.ch/filesender2/download.php?token=d6cba8dd-b844-47fb-aefe-2404ca503146&files_ids=26090",
        "1000" :  "https://filesender.switch.ch/filesender2/download.php?token=47471388-24bf-48b7-a28b-0a270c0f40c3&files_ids=26089"
    }

    for key in files:
        http_run(key, files[key])
    

 

