# Algorithms
# CLRS 

# Suppose we are comparing implementations of insertion sort and merge sort on the
# same machine. For inputs of size n, insertion sort runs in 8n2 steps, while merge
# sort runs in 64n lg n steps. For which values of n does insertion sort beat merge
# sort?

# Compare 8*n^2 to 64*n*log(n)
import math


n = 2
stop = 100
expression = True
print("Insertion sort beat merge sort for the following values of n:")
while n < stop:

    expression = n < 8 * math.log(n)/math.log(2)
    if expression:
        print("{}".format(n))
    else:
        break

    n += 1
    if n == stop:
        print("Reached STOP {}".format(stop))
