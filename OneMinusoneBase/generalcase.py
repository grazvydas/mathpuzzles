import numpy as np
from itertools import product

n = 20
a = []
for i in range(n):
    a.append(i % 2 * 2 -1)  # taking first vector (1, 1, ..., 1) finds only 4 vectors
A = [a]

allcases = product([-1, 1], repeat=n)

for case in allcases:
    if all(np.dot(np.array(A), case) == 0):
        A.append(case)
        print np.array(A).shape
        print np.array(A)

print 'We found %(no_perpendicular)s perpendicular vectors of dimension %(dimension)s' % \
      {'no_perpendicular': len(A),
       'dimension': str(n)}
print(np.array(A))
