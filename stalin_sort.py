# Stalin sort
# Check if the list is ordered, if it is not, remove the element.

import numpy as np


# Code
def stalin_sort(list_a):
    len_a = len(list_a)
    the_end = False
    i = 0
    j = i + 1
    while not the_end:
        if list_a[i] > list_a[j]:
            list_a.pop(j)
            len_a = len(list_a)
            if i == len_a - 1:
                the_end = True
        else:
            i += 1
            j += 1
            if j == len_a:
                the_end = True

    return list_a


# Input
n = 25  # Elements
A = np.random.randint(low=0, high=50, size=n)
A = list(A)
print(f"Input: {A}")

# Output
print(f"Output: {stalin_sort(A)}")
