import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
plt.style.use('seaborn-whitegrid')

x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)

rng = np.random.RandomState(0)

'''
plt.plot(x1, y1, 'o', color='black')
'''
#========================================
'''
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker, label="marker='{}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)
'''
#========================================
'''
plt.plot(x1, y1, '-ok', label="'-ok'")
'''
#========================================
'''
plt.plot(x1, y1, '-p', color='gray', markersize=15, linewidth=4, markerfacecolor='white', markeredgecolor='gray', markeredgewidth=2)
plt.ylim(-1.2, 1.2)
plt.legend(numpoints=1)
'''
#========================================
'''
plt.subplot(2, 1, 1)
plt.scatter(x1, y1, marker='o')
plt.subplot(2, 1, 2)
x2 = rng.randn(100)
y2 = rng.randn(100)
colors = rng.rand(100)
sizes = 1000*rng.rand(100)
plt.scatter(x2, y2, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar()
'''
#========================================

iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2, s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()
