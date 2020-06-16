import numpy as np


# Input
n = 15
A = np.random.randint(-50, 50, n)
print("Input A = {}".format(A))

# Code
for j in range(0, n-1, 1):
    small = A[j]
    index = j
    i = j + 1
    for i in range(i, n, 1):
        if A[i] < small:
            small = A[i]
            index = i
    A[index] = A[j]
    A[j] = small

# Output
print("Output A = {}".format(A))
