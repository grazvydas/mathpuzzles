import numpy as np
from itertools import product

n = 28

# straight forward 
def straight_forward(n, do_filter=True):
    allcases = product([-1, 1], repeat=n)
    if do_filter:
        allcases = filter(lambda x: sum(x)==0, allcases)
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
    nr = int(n/2)
    sample = np.array([1]*nr + [-1]*nr)

    while K < n:
        np.random.shuffle(sample)
        #new =  2*np.random.randint(2, size=n)-1
        if all(np.dot(np.array(A), sample) == 0):
            A.append(sample.copy())
            K += 1
            print(np.array(A).shape)
            print(np.array(A))

    print('We found %(no_perpendicular)s perpendicular vectors of dimension %(dimension)s' % \
         {'no_perpendicular': len(A), 'dimension': str(n)})
    print(np.array(A))



if __name__ == '__main__':
    random_vector(n)
    #straight_forward(n)
