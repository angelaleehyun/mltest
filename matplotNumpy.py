import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,10,0.1)
y = x **2


print(x)
print(y)


plt.plot(x,y,'ro')
plt.xlim(-10,10)
plt.ylim(0,100)
plt.show()