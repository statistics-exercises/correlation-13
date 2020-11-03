import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = np.zeros(100), np.zeros(100)
# Your code goes here



# This will draw the graph
plt.plot( xdata, ydata, 'bo')
xxx = np.linspace(0,1,100)
yyy = np.sin(4*xxx) + 0.1
yyy2 = np.sin(4*xxx) - 0.1
plt.plot( xxx, yyy, 'k-' )
plt.plot( xxx, yyy2, 'k-' )
plt.savefig("correlated_variables.png")
