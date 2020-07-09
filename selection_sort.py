# freeCodeCamp - Python for Data Science
# Course for Beginners (Learn Python, Pandas, NumPy, Matplotlib)

# Selection sort

import numpy as np

from search_min import search_min_value


# Code
def selection_sort(list_a, len_a):
    list_o = []
    while len_a >= 1:
        min_dict = search_min_value(list_a, len_a)
        list_o.append(min_dict['min_value'])
        list_a.pop(min_dict['index'])
        len_a = len(list_a)
    return list_o


if __name__ == "__main__":
    # Input
    n = 10  # Elements
    A = np.random.randint(low=0, high=50, size=n)
    A = list(A)
    print(f"Input: {A}")

    # Output
    print(f"Output: {selection_sort(A, n)}")
