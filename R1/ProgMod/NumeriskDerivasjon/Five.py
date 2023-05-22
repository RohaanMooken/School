import numpy as np
import matplotlib.pyplot as plt

def T(t):
    return ((70*np.e)**(-0.065*t))

def derivative(f, x, dx = 1e-8):
    return (f(x+dx)-f(x))/dx

def f(x):
    return derivative(T, x)

t = np.linspace(0, 60, 1000)

plt.plot(t, T(t), label="T")
plt.plot(t, f(t), label="f")

plt.legend()
plt.show()

print(t[41])