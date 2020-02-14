import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

x1 = np.linspace(0, 10, 100)

plt.plot(x1, np.sin(x1))

#plt.xlim(-1, 11)
plt.xlim(10, 0) # inverse 

plt.ylim(-1.5, 1.5)

#========================================
plt.axis([-1, 100, -1.5, 1.5])
plt.axis('tight')
plt.axis('equal')

plt.show()
