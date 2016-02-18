# info about backends!
#http://matplotlib.org/faq/usage_faq.html
import matplotlib
matplotlib.use('Qt4Agg')
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

A = [[ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
 [ 1, -1, -1,  1,  1, -1, -1, -1, -1,  1,  1,  1],
 [ 1,  1,  1, -1, -1, -1, -1, -1,  1,  1, -1,  1],
 [-1,  1, -1, -1,  1,  1, -1, -1,  1, -1,  1,  1],
 [-1,  1, -1,  1, -1, -1,  1, -1,  1,  1,  1, -1],
 [-1,  1,  1,  1, -1, -1, -1,  1, -1, -1,  1,  1],
 [ 1, -1,  1,  1, -1,  1, -1, -1,  1, -1,  1, -1],
 [ 1,  1,  1, -1,  1, -1,  1, -1, -1, -1,  1, -1],
 [-1, -1,  1, -1, -1,  1,  1, -1, -1,  1,  1,  1],
 [-1, -1,  1,  1,  1, -1,  1, -1,  1, -1, -1,  1],
 [-1, -1,  1, -1,  1, -1, -1,  1,  1,  1,  1, -1],
 [ 1, -1, -1, -1, -1, -1,  1,  1,  1, -1,  1,  1]]

M = np.array(A)
im = plt.imshow(M, interpolation="nearest")
plt.show()

while(True): 
    #a = raw_input()
    a = input()
    if a == 'quit':
        break
    if a not in ['c', 'r', 'sc', 'sr']:
        print('nope')
        continue

    #b = raw_input()
    b = input()
    c = 0
    try:
    	b = int(b)
    except:
        print('nope')
        continue
    if a in ['sc', 'sr']:
        #c = raw_input()
        c = input()
        try:
            c = int(c)
        except:
            print('nope')
       	    continue
    if b not in range(12) or c not in range(12):
        print('nope')
        continue
    
    if a == 'r':
        for i in range(12):
            A[b][i] = -A[b][i]            
    elif a == 'c':
        for i in range(12):
            A[i][b] = -A[i][b]
    elif a == 'sc':
        temp = []
        for i in range(12):
            temp.append(A[i][b])
        for i in range(12):
            A[i][b] = A[i][c]
        for i in range(12):
            A[i][c] = temp[i]
    else:
        temp = A[b]
        A[b] = A[c]
        A[c] = temp	
	
    M = np.array(A)
    im.set_data(np.array(A))
