import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.process_time()
        res = function(*args)
        print(time.process_time() - start_time)
        return res

    return wrapped
