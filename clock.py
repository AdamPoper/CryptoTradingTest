import time

class Clock:
    def __init__(self):
        self.start_time = time.perf_counter()
    
    def restart(self):
        self.start_time = time.perf_counter()

    def getElapsedTime(self):
        elapsed_time = time.perf_counter() - self.start_time
        return elapsed_time
