import queue
import socket
from queue import Queue


class SimpleSocket():
    def __init__(self, queue: Queue = queue.Queue()) -> None:
        self.port = 7777
        self.host = '127.0.0.1'
        self.stop_server = False
        self.queue: Queue = queue

    def send_message(self, msg: bytes):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.connect((self.host, self.port))
            soc.sendall(msg)
    
    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.bind((self.host, self.port))
            soc.listen()
            
            while not self.stop_server:
                conn, _ = soc.accept()
                data = conn.recv(1024)
                if data:
                    self.queue.put(data)
                    if self.queue.qsize() % 100 == 0:
                        print(self.queue.qsize())
                conn.sendall(data)