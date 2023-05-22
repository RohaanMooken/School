import matplotlib.pyplot as plt
import numpy as np

dx = 1E-8

def f(x):
    return x**2-4*x+5

def g(x):
    return np.e**x

def h(x):
    return (np.log(x))**1/2

def derivative(f, x):
    return (f(x+dx)-f(x))/dx

print(derivative(f, 1))
print(derivative(g, 1))
print(derivative(h, 1))