import time
import socket
import signal
from multiprocessing import Process
from generator import generate_vectors


def generate(host='127.0.0.1', port=65432, noise_enabled=False):    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            vectors = generate_vectors(1000)  
            count = 0
            for vector in vectors:
                count += 1
                s.sendall(vector)
            print('send', count)
            time.sleep(1)


def aggregate(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        with s.accept()[0] as conn:
            count = 0
            while True:
                data = conn.recv(1024)
                if not data:
                    count = 0
                    break
                count +=1
                if count % 1000 == 0:
                    print('chunk done')

                #conn.sendall(data)
            


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
    