import time

def timer(method):
    def inner(*args, **kwargs):
        startTime=time.time()
        result = method(*args, **kwargs)
        endTime=time.time()
        with open("time.txt", "w") as timef:
            timef.write("{} took {} seconds to do".format(method.__name__, endTime-startTime))
        return result
    return inner
