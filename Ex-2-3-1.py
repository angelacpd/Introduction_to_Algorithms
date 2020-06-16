# Merge sorting
# Page 31

import numpy as np
import math


# Input
n = 8
# A = np.random.randint(0, 50, n)
# A = [1, 2, 2, 3, 1, 2, 3, 6]
A = [1, 2, 2, 2, 1, 2, 3, 6]
print("Input A = {}".format(A))
p = 0
q = math.floor(len(A)/2)
r = len(A)

# Code
n1 = q - p + 1
n2 = r - q
L = [0] * n1
R = [0] * n2
print("n1 {}".format(n1))
print("len(L) {}".format(len(L)))

for i in range(0, n1, 1):
    L[i] = A[p + i]
for j in range(0, n2, 1):
    R[j] = A[q + j]

L[n1-1] = math.inf
R[n2-1] = math.inf

i = 0
j = 0
for k in range(p, r, 1):
    print("L[i] {}".format(L[i]))
    print("R[j] {}".format(R[j]))
    if L[i] <= R[j]:
        A[k] = L[i]
        i += 1
        print("i {}".format(i))
    elif A[k] == R[j]:
        j += 1
        print("j {}".format(j))
    # elif A[k] < R[j] and R[j] is not math.inf:
    #     A[k] = R[j]
    #     j += 1
    #     print("j {}".format(j))
    print("k {}".format(k))

    print("A[k] {}".format(A[k]))

# Output
print("Output A = {}".format(A))
