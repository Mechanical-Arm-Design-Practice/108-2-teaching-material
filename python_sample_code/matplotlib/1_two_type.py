import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 10, 100)

#matlab type
'''
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x1, np.sin(x1))
plt.subplot(2, 1, 2)
plt.plot(x1, np.cos(x1))
'''
#========================================
#object orientation type

fig, ax = plt.subplots(2)
ax[0].plot(x1, np.sin(x1))
ax[1].plot(x1, np.cos(x1))


plt.show()