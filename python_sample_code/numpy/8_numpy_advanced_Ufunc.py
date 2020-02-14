import numpy as np

np.random.seed(0)
'''
#Set output
x1 = np.arange(5)
y1 = np.empty(5)
y2 = np.zeros(10)
np.multiply(x1, 10, out=y1)
np.power(2, x1, out=y2[::2])

print(y1)
print(y2)

#========================================

#Aggregation
x2 = np.arange(1, 6)
print(np.add.reduce(x2))
print(np.multiply.reduce(x2))
print(np.add.accumulate(x2))
print(np.multiply.accumulate(x2))

#========================================

#cross
x3 = np.arange(1, 10)
print(np.multiply.outer(x3, x3))

#========================================

L = np.random.random(100)
#time it, please.

print(sum(L))

print(np.sum(L))

print(min(L), max(L))
print(np.min(L), np.max(L))
print(L.min(), L.max())
'''
#========================================

M = np.random.random((3, 4))
print(M)
print(M.sum())
print(M.min(axis=0))
print(M.max(axis=1))