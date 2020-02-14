import numpy as np
np.random.seed(1)
x1 = np.arange(10)
x2 = np.random.randint(10, size=(3, 4))

#========================================

print("x1:{}\n".format(x1))
print("x1[5:]:{}\n".format(x1[5:]))
print("x1[4:7]:{}\n".format(x1[4:7]))
print("x1[::2]:{}\n".format(x1[::2]))
print("x1[1::2]:{}\n".format(x1[1::2]))
print("x1[::-1]:{}\n".format(x1[::-1]))

#========================================

print("x2:{}\n".format(x2))
print("x2[:2, :3]:{}\n".format(x2[:2, :3]))
print("x2[:3, ::2]:{}\n".format(x2[:3, ::2]))
print("x2[::-1, ::-1]:{}\n".format(x2[::-1, ::-1]))
print("x2[:, 0]:{}\n".format(x2[:, 0]))
print("x2[0, :]:{}\n".format(x2[0, :]))

#========================================

print("x2:{}\n".format(x2))
x2_sub = x2[:2, :2]
print("x2_sub:{}\n".format(x2_sub))
x2_sub[0, 0] = 99
print("x2_sub:{}\n".format(x2_sub))
print("x2:{}\n".format(x2))

#========================================

print("x2:{}\n".format(x2))
x2_sub_copy = x2[:2, :2].copy()
print("x2_sub_copy:{}\n".format(x2_sub_copy))
x2_sub_copy[0, 0] = 42
print("x2_sub_copy:{}\n".format(x2_sub_copy))
print("x2:{}\n".format(x2))