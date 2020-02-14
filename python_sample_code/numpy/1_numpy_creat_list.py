import numpy as np

np.random.seed(1)

a = np.zeros((1,), dtype=int)

b = np.ones((3, 5), dtype=float)

c = np.full((3, 5), 3.14)

d = np.arange(0, 20, 2)

e = np.linspace(0, 1, 5)

f = np.random.random((3, 2))

g = np.random.normal(0, 1, (2, 3))

h = np.random.randint(0, 10, (1, 5))

i = np.eye(3)

j = np.empty((3, 3))

#========================================
'''
print("a :{}\n".format(a))
print("b :{}\n".format(b))
print("c :{}\n".format(c))
print("d :{}\n".format(d))
print("e :{}\n".format(e))
print("f :{}\n".format(f))
print("g :{}\n".format(g))
print("h :{}\n".format(h))
print("i :{}\n".format(i))
print("j :{}\n".format(j))
'''