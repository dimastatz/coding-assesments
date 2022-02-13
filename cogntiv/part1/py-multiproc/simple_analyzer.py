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
        self.marker: str = 'session_end'
        if start_worker:
            self.worker = threading.Thread(target=self.consume_queue)
            self.worker.start()
            
    def generate(self, size=1000, vec_size=50, is_noisy=False) -> Iterator[bytes]:
        for _ in range(size):
            if not is_noisy or not self.should_drop():
                yield pickle.dumps(np.random.normal(0, 0.1, vec_size))
        yield pickle.dumps(self.marker)

    def should_drop(self, interval=2000) -> bool:
        return np.random.randint(interval, size=1)[0] == 0

    def consume_queue(self):
        ac_rates, vectors = [], []
        while not self.force_exit:
            if self.queue.qsize() == 0:
                time.sleep(0.1)
            else:
                item = pickle.loads(self.queue.get())
                
                if isinstance(item, str) and item == self.marker:
                    ac_rates.append(len(vectors))
                    data_ac = len(vectors), np.mean(ac_rates), np.std(ac_rates)
                    
                    packet_loss = 'Packet Loss WARNING' if len(vectors) < 1000 else '' 
                    print('Acquisition stats (rate, mean, std) = ', data_ac, packet_loss)

                    vectors = []
                else:
                    vectors.append(item)

            
            
        
