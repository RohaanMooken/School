import math

a = -1
b = 1
h = 1E-6
x = a
sum = 0

def f(x):
    return (1-x**2)**(1/2)

def s(x):
    return (h**2 + k**2)**(1/2)

k = f(x + h) - f(x)

while x < b:
    sum += s(x)
    x += h

print(sum)