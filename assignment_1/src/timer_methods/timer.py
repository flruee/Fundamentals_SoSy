import time
import os

def execute_func_timer(timer_path, func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    with open(timer_path, "a") as f:
        f.write(f"{start}; {end}; {end-start}\n")
    return result

def ipfs_timer(func):
    def wrap(*args, **kwargs):
        timer_path = "results/"+func.__name__+".txt"
        folder = ("results")
        CHECK_FOLDER = os.path.isdir(folder)
        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(folder)
        return execute_func_timer(timer_path, func, *args, **kwargs)   
    return wrap

def http_timer(func):
    def wrap(*args, **kwargs):
        timer_path = "results/http/"+func.__name__+"_"".txt"
        folders_in_path = ["results", "results/http"]
        for folder in folders_in_path:
            CHECK_FOLDER = os.path.isdir(folder)
            # If folder doesn't exist, then create it.
            if not CHECK_FOLDER:
                os.makedirs(folder)       
        return execute_func_timer(timer_path, func, *args, **kwargs)   
    return wrap   

#Example...
#@timer
#def serialize():
#    print("serializing")

#@timer
#def store():
#    print("store")
