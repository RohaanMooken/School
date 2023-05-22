import numpy as np
import matplotlib.pyplot as plt

def T(t):
    return 70*np.e**-0.065*t

def newton(f, df, x0, tol=1e-6):
    if abs(f(x0)) < tol:
        return x0
    else:
        return newton(f, df, x0 - f(x0)/df(x0), tol)

t = np.linspace(0, 60, 1000)

