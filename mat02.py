import matplotlib.pyplot as plt

x = []
y = []

for i in range(10,-11,-1):
    x.append(i)
    y.append(i*i)
print(x)
print(y)


plt.plot(x,y,'ro')
plt.xlim(-10,10)
plt.ylim(0,100)
plt.show()
