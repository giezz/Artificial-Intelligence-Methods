import time

from functions import *

if __name__ == '__main__':
    city_amount = np.loadtxt("var3.txt", max_rows=1)
    A = np.loadtxt("var5.txt", skiprows=1)

    start = time.time()
    result = genetic_algorithm(50, 50, 0.5, A)
    end = time.time() - start
    a = np.zeros((result[:, 0].shape[0], result[:, 0].shape[0]))
    for i in range(result[:, 0].shape[0]):
        a[i] = result[:, 0][i].astype(np.ndarray)
    unique = np.unique(a, axis=0)
    for i in unique:
        print(f"path: {i} path cost: {path_cost(i, A)} ")
    print(f"время выполнения программы: {end}")
