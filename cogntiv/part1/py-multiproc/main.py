import time
import signal
from multiprocessing import Pool
from simple_socket import SimpleSocket
from simple_analyzer import SimpleAnalyzer


def generate(noise_enabled=False): 
    socket = SimpleSocket()
    analyzer = SimpleAnalyzer()
    while True:
        start = time.time()
        for vector in analyzer.generate():
            socket.send_message(vector)
        span = time.time() - start
        print('bunch send {}'.format(span))
        time.sleep(1 - span)
    

def aggregate():
    analyzer = SimpleAnalyzer(True)
    socket = SimpleSocket(analyzer.queue)
    socket.start_server()
   

def initializer():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


if __name__ == "__main__":
    try:
        pool = Pool(2, initializer=initializer)
        pool.apply_async(aggregate)
        pool.apply_async(generate)
        pool.close()
        input("Hit enter to terminate")
    except KeyboardInterrupt:
        pass
    finally:
        pool.terminate()
        pool.join()        
        print("Bye have a great time!")
    