import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

x1 = np.linspace(0, 10, 100)

plt.plot(x1, np.sin(x1 - 0), color='blue') #set by name
plt.plot(x1, np.sin(x1 - 1), color='g') #set by rgbcmyk
plt.plot(x1, np.sin(x1 - 2), color='0.75') #set by gray scale
plt.plot(x1, np.sin(x1 - 3), color='#FFDD44') #set by 16 bits code 
plt.plot(x1, np.sin(x1 - 4), color=(1.0, 0.2, 0.3)) #set by rgb turtle 
plt.plot(x1, np.sin(x1 - 5), color='chartreuse') #set by HTML support
#========================================
plt.plot(x1, x1 + 0, linestyle='solid')
plt.plot(x1, x1 + 1, linestyle='dashed')
plt.plot(x1, x1 + 2, linestyle='dashdot')
plt.plot(x1, x1 + 3, linestyle='dotted')
#========================================
plt.plot(x1, x1 + 4, linestyle='-')
plt.plot(x1, x1 + 5, linestyle='--')
plt.plot(x1, x1 + 6, linestyle='-.')
plt.plot(x1, x1 + 7, linestyle=':')
#========================================
plt.plot(x1, x1 + 8, '-g')
plt.plot(x1, x1 + 9, '--c')
plt.plot(x1, x1 + 10, '-.k')
plt.plot(x1, x1 + 11, ':r')
#========================================
plt.show()

