# Bubblesort Algorithm
# Page 40 - Problem 2-2

import numpy as np


# Input
n = 10
A = np.random.randint(0, 20, n)
print(f"Input A = \n{A}")

# Code
ALength = len(A)
for i in range(0, ALength - 1):
    for j in range(ALength-1, i, -1):
        if A[j] < A[j-1]:
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp

# Output
print(f"Output A = \n{A}")
