import math
import matplotlib.pyplot as plt

yData = []
xData = []

for i in range(0,11):
    y = i**2
    yData.append(y)
    xData.append(i)

plt.plot(xData, yData)
plt.show()
#go to main repo?