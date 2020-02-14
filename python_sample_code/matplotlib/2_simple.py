import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

x1 = np.linspace(0, 10, 100)
'''
fig = plt.figure()
ax = plt.axes()
ax.plot(x1, np.sin(x1))

'''
#========================================
'''
plt.plot(x1, np.sin(x1))
plt.plot(x1, np.cos(x1))
'''
plt.show()
