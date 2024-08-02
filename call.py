import time

class Timer:
    def __init__(self, func):
        self.func = func


    def __call__(self, *args, **kwargs):
        start_time = time.time()
        print('do some func')
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f'func worked {end_time - start_time}')
        return result



@Timer
def calculate():
    for i in range(100000000):
        2**100


calculate()