import numpy as np

x = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Array {}".format(x))
print("Type {}".format(type(x)))
print("Size of array {}".format(x.shape))
print("Row {}".format(x[1]))
print("Element {}".format(x[1][2]))

y = np.array([[[1, 2, 3],
               [4, 5, 6]],
              [[6, 7, 8],
               [9, 10, 11]]])
print("Tensor {}".format(y))
print("Shape tensor {}".format(y.shape))

z = y.T
print("Transpose tensor {}".format(z))

print("Create vector {}".format(np.arange(5)))
print("Print column {}".format(x[:, 2]))
print("Print elements of a column {}".format(x[:, [1, 2, 0, 0, 0]]))
