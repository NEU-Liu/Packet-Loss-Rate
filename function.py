import matplotlib.pyplot as plt
import numpy as np
import math


def func1(x):
    return 1 - math.sqrt(x)


def func2(x):
    return 0.5 * (1 - x)


x = np.linspace(0, 1, 500)
y1 = []
for i in range(500):
    unit = 0.1/500
    y1.append(func1(unit*i))

y2 = []
for i in range(500):
    unit = 0.1/500
    y2.append(func2(unit*i))

plt.plot(x, y1, color='r', label='1-math.sqrt(s/n)')
plt.plot(x, y2, '-.', color='b', label='0.5x(1-s/n)')

plt.legend()

plt.savefig('com.png')
