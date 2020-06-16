# Binary Search
# Page 39 - Exercise 2.3-5

import numpy as np
import math


# Input
v = int(input("Type an integer from 0 to 100. v = "))
A = np.random.randint(0, 200, 200)
print(f"Input: A = \n{A}")
ALength = len(A)

# Insertion sort algorithm
for j in range(0, ALength):
    key = A[j]
    # Insert A[j] into the sorted sequence A[1 .. j-1]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
print(f"Sorted: A = \n{A}")

# Binary search
result = "'v' is not in A."
a1 = 0
a2 = ALength - 1
am = math.floor(ALength/2)
j = 0   # force break while
while (a2 - a1) >= 1 and j <= 20:
    if v < A[am]:
        a2 = am
    elif v > A[am]:
        a1 = am
    else:  # v = A[index]
        result = "v is in index = " + str(am)
        break
    am = math.floor((a2 - a1) / 2)
    am = a1 + am
    print(f"am = {am}\na1 = {a1}\na2 = {a2}\n")

    j += 1  # force break while

# Output
print(f"{result}")
