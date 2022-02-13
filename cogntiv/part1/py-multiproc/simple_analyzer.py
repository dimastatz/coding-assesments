import os
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
        self.report_file: str = self.get_report_file()
        self.matrix = None

        if start_worker:
            self.worker = threading.Thread(target=self.consume_queue)
            self.worker.start()
            
    def generate(self, size=1000, vec_size=50, is_noisy=False) -> Iterator[bytes]:
        for _ in range(size):
            if not self.should_drop(is_noisy):
                yield pickle.dumps(np.random.normal(0, 0.1, vec_size))
        yield pickle.dumps(self.marker)

    def get_report_file(self):
        return '{}-{}.txt'.format(os.getcwd(), time.time_ns() // 1000)

    def should_drop(self, is_noisy: bool, interval=3000) -> bool:
        return np.random.randint(interval, size=1)[0] == 0 if is_noisy else False
    
    def is_marker(self, item) -> bool:
        return isinstance(item, str) and item == self.marker
    
    def consume_queue(self):
        ac_rates, vectors = [], []
        while not self.force_exit:
            if self.queue.qsize() == 0:
                time.sleep(0.1)
            else:
                item = pickle.loads(self.queue.get())
                if self.is_marker(item):
                    ac_rates.append(len(vectors))
                    self.submit_report(ac_rates, vectors)
                    vectors.clear()
                    self.matrix = None
                else:
                    if self.matrix is None:
                        self.matrix = np.array([item])
                    else:
                        self.matrix = np.vstack([self.matrix, item])

                    vectors.append(item)
    
    def submit_report(self, ac_rates, vectors):
        packet_loss = 'Packet Loss WARNING' if len(vectors) < 1000 else '' 
        report = 'Acquisition rate={}, mean={}, std={}. {}'.format(
            len(vectors), np.mean(ac_rates), np.std(ac_rates), packet_loss)

        with open(self.report_file, 'a') as f:
            print(report)
            f.writelines([report, '\n'])
            

    
            
        
