import numpy
import pickle
import threading
from queue import Queue
from typing import Iterator

class SimpleAnalyzer():
    def __init__(self, start_worker=False) -> None:
        self.force_exit = False
        self.queue: Queue = Queue()
        if start_worker:
            self.worker = threading.Thread(target=self.consume_queue)
            self.worker.start()
            
    
    def generate(self, size: int = 1000) -> Iterator[bytes]:
        for _ in range(size):
            vector = [1] * 50
            yield pickle.dumps(vector)

    def consume_queue(self):
        try:
            count = 0
            while not self.force_exit:
                item = self.queue.get()
                if item:
                    vector = pickle.loads(item)
                    count +=1
                if count % 100 == 0:
                    print('consume', count, vector)
        except KeyboardInterrupt:
            exit(0)


