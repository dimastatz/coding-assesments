import sys
import time
import signal
import numpy as np
from multiprocessing import Pool
from simple_socket import SimpleSocket
from simple_analyzer import SimpleAnalyzer


def generate(is_noisy: bool): 
    socket = SimpleSocket()
    analyzer = SimpleAnalyzer()
    while True:
        start = time.time()
        for vector in analyzer.generate(is_noisy=is_noisy):
            socket.send_message(vector)
        span = time.time() - start
        time.sleep(1 - span)
    

def aggregate():
    analyzer = SimpleAnalyzer(True)
    socket = SimpleSocket(analyzer.queue)
    socket.start_server()
   

def initializer():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


if __name__ == "__main__":
    try:
        
        is_noisy = True if 'add_noise' in sys.argv else False
        pool = Pool(2, initializer=initializer)
        pool.apply_async(aggregate)
        pool.apply_async(generate, kwds={'is_noisy': bool(is_noisy)})
        pool.close()
        input('Started with noisy={}. Press any key to exit\n'.format(is_noisy))
    except KeyboardInterrupt:
        pass
    finally:
        pool.terminate()
        pool.join()        
        print("Py-Multiproc Test is Exiting!")
        exit(0)
    