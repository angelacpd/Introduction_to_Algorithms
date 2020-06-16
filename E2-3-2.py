# Merge sorting
# Page 38 - my code

import math


# Input
# A = [1, 2, 2, 3, 1, 2, 3, 6]
# A = [1, 2, 3, 6, 1, 2, 2, 3]
# A = [2, 2, 2, 2, 1, 2, 3, 6]
# A = [1, 2, 3, 6, 2, 2, 2, 2]
# A = [1, 2, 3, 6, 16, 2, 2, 7, 10, 12, 15]
A = [2, 2, 7, 10, 15, 1, 2, 4, 5, 8, 16]
print("Input A = {}".format(A))
p = 0
q = math.floor(len(A)/2)
r = len(A)

# Code
n1 = q - p
n2 = r - q
L = [0] * n1
R = [0] * n2

for i in range(0, n1, 1):
    L[i] = A[p + i]
for j in range(0, n2, 1):
    R[j] = A[q + j]
print("L[i] {}".format(L))
print("R[j] {}".format(R))

i = 0
j = 0
iMax = len(L) - 1
jMax = len(R) - 1
for k in range(p, r):

    if i <= iMax and j <= jMax:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    elif i > iMax:
        A[k:r-1] = R[j:n2-1]
        break
    elif j > jMax:
        A[k:r-1] = R[i:n1-1]
        break

# Output
print("Output A = {}".format(A))
print(f"Output A = {A}")
