a = -1
b = 1
N = 1000
h = 0.002
S = 0
sum = 0
 
import numpy as np

d = 1/1000
teller = -1
 
def g(x):
    return np.sqrt(1-x**2)
 
def x(i):
    return -1 + i*h
 
def k(i):
    return g(x(i+1)) - g(x(i))
 
for i in range(N):
    S = np.sqrt(h**2 + (k(i)**2))
    sum += S
    teller += d
 
print(sum)