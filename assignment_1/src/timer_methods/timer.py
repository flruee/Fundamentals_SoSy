
def timer(func):
    def wrap(*args, **kwargs):

        timer_path = "results/"+func.__name__+".txt"

        MYDIR = ("results")
        CHECK_FOLDER = os.path.isdir(MYDIR)

        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.makedirs(MYDIR)
            
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        with open(timer_path, "a") as f:
            f.write(str(start)+";"+str(end)+"\n")
        return result

    return wrap

#Example...
#@timer
#def serialize():
#    print("serializing")

#@timer
#def store():
#    print("store")
