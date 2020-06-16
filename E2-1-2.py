# Insertion-Sort (A) non-decreasing order

A = [31, 41, 59, 26, 41, 58]    # E 2.1-1
ALength = len(A)

for j in range(0, ALength):
    print(j)
    key = A[j]
    # Insert A[j] into the sorted sequence A[1 .. j-1]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
    print(A)

# E 2.1-2
# Insertion-Sort (A) non-increasing order
A = [5, 2, 4, 6, 1, 3]

ALength = len(A)

for j in range(0, ALength):
    print(j)
    key = A[j]
    # Insert A[j] into the sorted sequence A[1 .. j-1]
    i = j - 1
    while i >= 0 and A[i] < key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
    print(A)
