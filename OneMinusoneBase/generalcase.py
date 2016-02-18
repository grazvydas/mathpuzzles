import numpy as np
from itertools import product

n = 20


# straight forward 
def straight_forward(n):
    allcases = product([-1, 1], repeat=n)
    a = []
    for i in range(n):
        a.append(i % 2 * 2 -1)  # taking first vector (1, 1, ..., 1) finds only 4 vectors
    A = [a]
    for case in allcases:
        if all(np.dot(np.array(A), case) == 0):
            A.append(case)
            print(np.array(A).shape)
            print(np.array(A))
    print('We found %(no_perpendicular)s perpendicular vectors of dimension %(dimension)s' % \
          {'no_perpendicular': len(A), 'dimension': str(n)})
    print(np.array(A))


def random_vector(n):
    K = 1
    a = [1]*n
    A = [a]

    while K < n:
        new =  2*np.random.randint(2, size=n)-1
        if all(np.dot(np.array(A), new) == 0):
            A.append(new)
            K += 1
            print(np.array(A).shape)
            print(np.array(A))

    print('We found %(no_perpendicular)s perpendicular vectors of dimension %(dimension)s' % \
         {'no_perpendicular': len(A), 'dimension': str(n)})
    print(np.array(A))



if __name__ == '__main__':
    random_vector(28)
