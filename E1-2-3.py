# Algorithms
# CLRS

# What is the smallest value of n such that an algorithm whose running time is 100n2
# runs faster than an algorithm whose running time is 2n on the same machine?

stop = 100
n = 1
while n < stop:
    expression = 100 * (n**2) > 2**n
    if expression:
        print("n: {}    100n^2: {}  2^n: {}".format(n, 100*(n**2), 2**n))
    else:
        break
    n += 1

# Answer: n = 15
