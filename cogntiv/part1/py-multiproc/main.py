import time
import signal
import queue
from multiprocessing import Process
from simple_socket import SimpleSocket


def generate(noise_enabled=False):  
    socket = SimpleSocket()
    while True:
        for i in range(1000):
            socket.send_message(b'hello world')
        print('bunch send')
        time.sleep(1)
    


def aggregate(host='127.0.0.1', port=65432):
    q = queue.Queue()
    socket = SimpleSocket(q)
    socket.start_server()
   
    
def main():
    try:
        Process(target=aggregate, name='aggregator').start()
        Process(target=generate, name='generator').start()
    except:
        exit(0)

def exit_handler(signum, frame):
    print('Ctrl+Z pressed, but ignored {} {}'.format(signum, frame))
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTSTP, exit_handler)
    main()
    