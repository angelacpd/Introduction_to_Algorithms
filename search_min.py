# freeCodeCamp - Python for Data Science
# Course for Beginners (Learn Python, Pandas, NumPy, Matplotlib)

# Search minimum

import numpy as np


# Code
def search_min_value(list_a, len_a):
    min_value = list_a[0]
    index = 0
    counter = 1
    while counter <= len_a - 1:
        v = list_a[counter]
        if v < min_value:
            min_value = v
            index = counter
        counter += 1
    return {'min_value': min_value, 'index': index}
    # return min_value, index


if __name__ == "__main__":
    # Input
    n = 10  # Elements
    A = np.random.randint(low=0, high=50, size=n)
    A = list(A)
    print(A)

    # Output
    print(search_min_value(A, n))
    # min_v, idx = search_min_value(A, n)
    # print(min_v)
    # print(idx)

