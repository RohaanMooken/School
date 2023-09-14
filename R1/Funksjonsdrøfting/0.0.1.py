import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Toppunkt, Bunnpunkt, monotoniegenskaper, krumning og vendepunkt

a = -3
b = 3
h = 0.00001

nullpunkter = []

def f(x):
    return x**3-5*x-3

def Df(x):
    return (f(x+h)-f(x))/h

def DDf(x):
    return (Df(x+h)-Df(x))/h

def pp(x, y):
    plt.plot(x, y, marker=".", markersize=10, markerfacecolor="red")

def samesign(a, b):
        return a * b > 0

def bisect(a, b):
    
    assert not samesign(f(a), f(b)), "[ERROR] a and b variables are of the same sign"

    for i in range(54):
        c = (a+b)/2
        if samesign(f(a), f(c)):
            a = c
        else:
            b = c

    return c

# roots = fsolve(f,[x for x in range(a, b+1)])
# print(roots)

# for root in roots:
#     pp(root, f(root))


x = np.linspace(a, b, 1000)

# for i in range(-3, -2):
#     print(i)
#     nullpunkter.append(bisect(i, abs(i)))

# for nullpunkt in nullpunkter:
#     pp(nullpunkt, f(nullpunkt))

nullpunkt = bisect(a,b)
pp(nullpunkt, f(nullpunkt))

plt.plot(x, f(x), label="f(x)")
plt.plot(x, Df(x), label="f'(x)")
plt.plot(x, DDf(x), label="f''(x)")

plt.plot()

plt.legend()
plt.grid()
plt.show()
