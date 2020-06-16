# Horner's rule
# Page 41 - Problem 2-3

# Input
x = 2
a = [5, 4, 3, 2]
print(f"x = {x}\n")
print(f"a = {a}\n")

# Code
y = 0
for i in range(len(a)-1, -1, -1):
    y = a[i] + x*y
    print(y)

# Output
print(f"y = {y}\n")
