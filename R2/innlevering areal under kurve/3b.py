# Høyre metoden

import math

a = -2
b = 2
n = 100
dx = (b - a) / n

x = a + dx
sum = 0
i = 0

def f(x):
    return 3*math.e**(-(x**2)/2)

while x < b + dx:
    sum += f(x) * dx
    x += dx
    print(i)
    i += 1

print(sum)