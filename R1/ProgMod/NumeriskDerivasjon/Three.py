import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + 1/3 * x

def derivative(f, x, dx = 1E-8):
    return (f(x+dx)-f(x))/dx

def g(x):
    return derivative(f, x)

def h(x):
    return derivative(g, x)

x = np.linspace(0, 10, 100)

plt.plot(x, f(x), label="x")
plt.plot(x, g(x), label="xx")
plt.plot(x, h(x), label="xxx")

plt.legend()
plt.show()