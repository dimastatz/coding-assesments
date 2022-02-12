import queue
import pickle
import threading
import time

class Aggregator():
    def __init__(self) -> None:
        self.data = queue.Queue(10000)
        
    def add_item(self, item):
        self.data.put(item, block=False)
        if self.data.full():
            print('Queue is Full')
            self.data.empty()

    def aggregate(self):
        count = 0
        while not self.data.empty():
            count += 1
            item = self.data.get_nowait()
        
        print('queue is empty {}'.format(count))
        count = 0
           
            