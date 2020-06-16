# Code for exercise 2.1-3

# LINEAR SEARCH
import numpy as np

# Inputs
n = 10
A = np.random.randint(low=0, high=50, size=n)
print("A = {}".format(A))
v = 17
ALength = len(A)

# Code
index = "NIL"
for i in range(0, ALength):
    if v == A[i]:
        index = i
        break

# Output
print("Index is: {}".format(index))
