import numpy as np
from itertools import product
import time
import sys

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
            #print(np.array(A))

    print('We found %(no_perpendicular)s perpendicular vectors of dimension %(dimension)s' % \
         {'no_perpendicular': len(A), 'dimension': str(n)})
    print(np.array(A))

def random_vector_with_replacement(n):
    K = 1
    a = [1]*n
    A = [a]
    nr = int(n/2)
    sample = np.array([1]*nr + [-1]*nr)

    while K < n:
        np.random.shuffle(sample)
        #new =  2*np.random.randint(2, size=n)-1
        where = np.flatnonzero(np.dot(np.array(A), sample))
        if len(where)==0: 
            A.append(sample.copy())
            K += 1
            print(np.array(A).shape)
            #print(np.array(A))
        elif len(where)==1:
            A[where[0]] = sample.copy()
            print("-", end="", flush=True)
            #print(np.array(A).shape)
            #print(np.array(A))
            
    print('We found %(no_perpendicular)s perpendicular vectors of dimension %(dimension)s' % \
         {'no_perpendicular': len(A), 'dimension': str(n)})
    print(np.array(A))

# count execution time
def test_execution():
    n = 20
    NUM_OF_TRIALS = 5
    start_time = time.time()
    for i in range(NUM_OF_TRIALS):
        print(" %s is started " % i)
        random_vector_with_replacement(n)
        print(" %s is done " % i)
    v1_time = time.time() - start_time
    start_time = time.time()
    for i in range(NUM_OF_TRIALS):
        print(" %s is started " % i)
        random_vector(n)
        print(" %s is done " % i)
    v2_time = time.time() - start_time

    print("--- with replacment version takes %s seconds ---" % v1_time) 
    print("--- with no replacment version takes %s seconds ---" % v2_time) 


if __name__ == '__main__':
    #straight_forward(n)
    random_vector_with_replacement(n)
    #random_vector(20)
    #test_execution()
