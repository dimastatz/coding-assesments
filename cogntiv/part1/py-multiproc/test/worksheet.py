import numpy as np

M = None

for i in range(5):
    V = np.random.normal(0, 0.1, 3)
    if M is None:
        M = np.array([V])
    else:
        M = np.vstack([M, V])

    print(M, M.shape[0])