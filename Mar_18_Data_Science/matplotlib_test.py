import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10)
y = np.sqrt(x)

#fig, ax = plt.subplots()
#ax.plot(x, y)
plt.plot(x, y)

#ax.set(xlabel='number (x)', ylabel='square root',
#       title='Square roots of numbers')
#ax.grid()

#fig.savefig("test.png")
plt.show()