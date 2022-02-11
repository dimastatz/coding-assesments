import time
import socket
import signal
from multiprocessing import Process


def generate_vectors(length: int) -> list:
    res = []
    for i in range(length):
        res.append([1] * 50)
    return res


def simulate_noise(vectors: list) -> list:
    return vectors


def generate(host='127.0.0.1', port=65432, noise_enabled=False):    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            vectors = generate_vectors(1000)
            vectors = simulate_noise(vectors) if noise_enabled else vectors   
            s.sendall(b'Hello, world')
            time.sleep(1)


def aggregate(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        with s.accept()[0] as conn:
            while True:
                data = conn.recv(1024)
                print('aggre', data)
                if not data:
                    break
                conn.sendall(data)


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
    