import numpy as np


def get_matrix_stats(matrix: np.array) -> list:
    res = []
    for i in range(matrix.shape[1]):
        column = matrix[:, i]
        res.append((np.mean(column), np.std(column)))
    return res


M = None

for i in range(5):
    V = np.random.normal(0, 0.1, 3)
    if M is None:
        M = np.array([V])
    else:
        M = np.vstack([M, V])

print(M, M.shape[0])
get_matrix_stats(M)