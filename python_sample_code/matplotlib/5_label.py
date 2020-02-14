import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

x1 = np.linspace(0, 10, 100)

'''
plt.plot(x1, np.sin(x1))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)")
'''
#========================================
'''
plt.plot(x1, np.sin(x1), '-g', label='sin(x)')
plt.plot(x1, np.cos(x1), ':b', label='cos(x)')

plt.axis('equal')
plt.legend()
'''
#========================================

ax = plt.axes()
ax.plot(x1, np.sin(x1))
ax.set(xlim=(0, 10), ylim=(-2, 2), xlabel='x', ylabel='sin(x)', title='A Simple Plot')

plt.show()
