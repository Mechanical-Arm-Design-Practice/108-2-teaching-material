import numpy as np

x1 = np.random.randint(-100, 100, size=(1,))
x2 = np.random.randint(-100, 100, size=(3,4))
x3 = np.random.randint(-100, 100, size=(3,4,5))

#========================================

print("x3 ndim:{}\n".format(x3.ndim))
print("x3 shape:{}\n".format(x3.shape))
print("x3 size:{}\n".format(x3.size))
print("x3 dtype:{}\n".format(x3.dtype))
print("x3 itemsize:{} bytes\n".format(x3.itemsize))
print("x3 nbytes:{} bytes\n".format(x3.nbytes)) #nbytes = itensize*size

