import numpy as np
import time as t
np.random.seed(1)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0/values[i]
    return output

values = np.random.randint(1, 10, size=5)

time1 = t.time()
print(compute_reciprocals(values))
time2 = t.time() - time1 

time3 = t.time()
print(1.0/values)
time4 = t.time() - time3

print(time2)
print(time4)

#========================================

print(np.arange(5)*np.arange(1, 6))

#========================================

x1 = np.arange(4)
x2 = np.array([-2, -1, 0, 1, 2])
x3 = np.array([3-4j, 4-3j, 2+0j, 0+1j])

print("x1:{}\n".format(x1))
print("x1+5:{}\n".format(x1+5))
print("x1/5:{}\n".format(x1/5))
print("x1//2:{}\n".format(x1//2))
print("x1**2:{}\n".format(x1**2))
print("-x1:{}\n".format(-x1))
print("x1%2:{}\n".format(x1%2))

#python built-in function
print("abs(x2):{}\n".format(abs(x2)))
print("np.absolute(x2):{}\n".format(np.absolute(x2)))
print("np.abs(x2):{}\n".format(np.abs(x2)))
print("np.abs(x3):{}\n".format(np.abs(x3)))

#========================================
theta = np.linspace(0, np.pi, 3)
x1 = np.array([-1, 0, 1])

print("theta:{}\n".format(theta))
print("sin(theta):{}\n".format(np.sin(theta)))
print("cos(theta):{}\n".format(np.cos(theta)))
print("tan(theta):{}\n".format(np.tan(theta)))

print("x1:{}\n".format(x1))
print("arcsin(theta):{}\n".format(np.arcsin(x1)))
print("arccos(theta):{}\n".format(np.arccos(x1)))
print("arctan(theta):{}\n".format(np.arctan(x1)))

#========================================

x1 = np.array([1, 2, 3])
print("x1:{}\n".format(x1))
print("e^x:{}\n".format(np.exp(x1)))
print("2^x:{}\n".format(np.exp2(x1)))
print("3^x:{}\n".format(np.power(3, x1)))

x2 = np.array([1, 2, 4, 10])
print("x2:{}\n".format(x2))
print("ln(x2):{}\n".format(np.log(x2)))
print("log2(x2):{}\n".format(np.log2(x2)))
print("lop10(x2):{}\n".format(np.log10(x2)))

#========================================
