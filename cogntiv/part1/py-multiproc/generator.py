import pickle
import datetime

def generate_vectors(num: int, noise=True) -> bytes:
    res = []
    for _ in range(num):
        vector = [1]*50
        res.append(pickle.dumps(vector))
    return res



