import numpy as np

u = np.array([0, 0, 0])
v = np.array([0, 0, 0])

u[0] = int(input("Hva er x verdien i u vektoren? "))
u[1] = int(input("Hva er y verdien i u vektoren? "))
u[2] = int(input("Hva er z verdien i u vektoren? "))
v[0] = int(input("Hva er x verdien i v vektoren? "))
v[1] = int(input("Hva er y verdien i v vektoren? "))
v[2] = int(input("Hva er z verdien i v vektoren? "))

print(u + v)
print(u - v)
print(2 * u + 3 * v)
print(u[0], v[1])