import time
import pickle
import threading
import numpy as np
from queue import Queue
from typing import Iterator


class SimpleAnalyzer():
    def __init__(self, start_worker=False) -> None:
        self.force_exit = False
        self.queue: Queue = Queue()
        if start_worker:
            self.worker = threading.Thread(target=self.consume_queue)
            self.worker.start()
            
    
    def generate(self, size=1000, vec_size=50) -> Iterator[bytes]:
        for _ in range(size):
            yield pickle.dumps(np.random.normal(0, 0.1, vec_size))


    def consume_queue(self):
        ac_rates = []
        while not self.force_exit:
            start = time.time()
            vectors = []
            while self.queue.qsize() > 0:
                item = self.queue.get()
                vectors.append(pickle.loads(item))
            
            ac_rates.append(len(vectors))
            data_ac = len(vectors), np.mean(ac_rates), np.std(ac_rates)
            print('data acquisition (rate, mean, std) = ', data_ac)

            if len(vectors) < 1000:
                print('packet loss WARNING')

            time.sleep(1 - (time.time() - start))
            
            
        
