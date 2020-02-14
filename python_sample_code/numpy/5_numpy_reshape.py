import numpy as np

grid = np.arange(1, 10).reshape((3, 3))
print("grid:{}\n".format(grid))

x1 = np.array([1, 2, 3])

x1_reshape1 = x1.reshape(1, 3)
x1_reshape2 = x1.reshape(3, 1)

x1_reshape3 = x1[np.newaxis, :]
x1_reshape4 = x1[:, np.newaxis]

#========================================

print("x1:{}\n".format(x1))
print("x1_reshape1:{}\n".format(x1_reshape1))
print("x1_reshape2:{}\n".format(x1_reshape2))
print("x1_reshape3:{}\n".format(x1_reshape3))
print("x1_reshape4:{}\n".format(x1_reshape4))

