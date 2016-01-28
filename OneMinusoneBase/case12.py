import numpy as np
from itertools import product

A = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1],
    [1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1],
    [1, -1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1],
    [-1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1],
    [-1, -1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1],
    [-1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1],
    [-1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1],
    [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1],
    [-1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1],
    [-1, 1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1]])


allcases = product([-1, 1], repeat=12)

print(A)
print(A.shape)
print(np.dot(A, A.T))
ATS = []
for case in allcases:
    if all(np.dot(A, case) == 0):
        ATS.append(case)


print(len(ATS))
for a in ATS:
    print(a)

