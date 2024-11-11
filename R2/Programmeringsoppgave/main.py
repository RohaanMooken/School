import numpy as np

def g(x):
    return np.sqrt(1 - x**2)

def lengde(a, b, N):
    h = (b - a) / N
    total_lengde = 0

    for i in range(N):
        x_i = a + i * h
        x_ip1 = a + (i + 1) * h
        
        k_i = g(x_ip1) - g(x_i)
        
        S_i = np.sqrt(h**2 + k_i**2)
        
        total_lengde += S_i
    
    return total_lengde

a = -1
b = 1
N = 1000

lengde = lengde(a, b, N)
print(f"{lengde:.5f}")
print(np.pi)