# Trapes metoden

import math

a = -2
b = 2
n = 100
dx = (b - a) / n
z = 1

x = a + (z - 1) * dx
sum = 0

def f(x):
    return 3*math.e**(-(x**2)/2)

while x < b:
    sum += (f(a + (z - 1) * dx) + f(a + (z) * dx)) / 2 * dx
    x += dx
    z += 1

print(sum)