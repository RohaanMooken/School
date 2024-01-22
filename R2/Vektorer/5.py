# A) h + k er katetene til trekanten, tar vi kvadratroten av dem finner vi hypotenusen som i dette tilfellet er lengden av grafen i ntervalelt [i, i+1]

import math

a = -1
b = 1
dx = 0.001
length = 0

def g(x):
    return math.sqrt(1 - x**2)

while a <= b:
    length += math.sqrt(dx**2 + (g(round(a + dx, 3)) - g(a))**2)
    a += dx
print(length)