import math

a = -2
b = 2
n = 100
dx = (b - a) / n

x = a
sum = 0

def f(x):
    return 3*math.e**(-(x**2)/2)

# for i in range(a, b,):
#     sum += f(i)*dx

while x < b:
    sum += f(x) * dx
    x += dx

print(sum)

##### Bruk formel i boka venstremetoden