import numpy as np

x1 = np.arange(0, 20, 2)
x2 = np.array([range(i, i+3) for i in [1, 4, 7] ])

#========================================

print("x1 :{}\n".format(x1))
print("x1[0] :{}\n".format(x1[0]))
print("x1[4] :{}\n".format(x1[4]))
print("x2 :{}\n".format(x2))
print("x2[0, 0] :{}\n".format(x2[2, 0]))
print("x2[0, -1] :{}\n".format(x2[0, -1]))

x2[0, -1] = 100

print("x2[0, -1] :{}\n".format(x2))

#!!!
x2[0, -1] = 3.14

print("x2[0, -1] :{}\n".format(x2))
