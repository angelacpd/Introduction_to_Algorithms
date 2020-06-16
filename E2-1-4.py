# Code for exercise 2.1-4

# Input: Two sequences of n elements A = <a1, a2, ..., an> and B <b1, b2, ..., bn> representing two
# n-bit binary integers.

# Output: The sum of the two input sequences as a (n+1)-element array C representing (n+1)-bit
# binary integer.

import numpy as np

# Inputs
n = 4
A = np.random.randint(low=0, high=2, size=n)
B = np.random.randint(low=0, high=2, size=n)
print("A = {}".format(A))
print("B = {}".format(B))
C = [0] * (n+1)

# Code
bit_carry = 0
for i in range(n-1, -1, -1):
    bit_sum = A[i] + B[i] + bit_carry
    if bit_sum == 0:
        C[i+1] = 0
        bit_carry = 0
    elif bit_sum == 1:
        C[i + 1] = 1
        bit_carry = 0
    elif bit_sum == 2:
        C[i + 1] = 0
        bit_carry = 1
    else:
        C[i + 1] = 1
        bit_carry = 1
C[0] = bit_carry

# Output
print("C = {}".format(C))
