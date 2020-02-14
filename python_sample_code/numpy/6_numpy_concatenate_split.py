import numpy as np

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.array([99, 99, 99])
grid = np.arange(1, 10).reshape((3, 3))
grid2 = np.arange(16).reshape((4, 4))

cancatenate_1 = np.concatenate([x, y])
cancatenate_2 = np.concatenate([x, y, z])
cancatenate_3 = np.concatenate([grid, grid], axis=0)
cancatenate_4 = np.concatenate([grid, grid], axis=1)
cancatenate_5 = np.vstack([x, grid])
cancatenate_6 = np.hstack([x.reshape(3, 1), grid])

#========================================

print("cancatenate_1:{}\n".format(cancatenate_1))
print("cancatenate_2:{}\n".format(cancatenate_2))
print("cancatenate_3:{}\n".format(cancatenate_3))
print("cancatenate_4:{}\n".format(cancatenate_4))
print("cancatenate_5:{}\n".format(cancatenate_5))
print("cancatenate_6:{}\n".format(cancatenate_6))

#========================================

print("cancatenate_2:{}\n".format(cancatenate_2))
x1, x2, x3 = np.split(cancatenate_2, [3, 5])
print("x1:{}, x2:{}, x3:{}".format(x1, x2, x3))

print("grid2:{}\n".format(grid2))

upper, lower = np.vsplit(grid2, [2])
print("upper:{}\nlower:{}\n".format(upper, lower))

left, right = np.hsplit(grid2, [2])
print("left:{}\nright:{}".format(left, right))
