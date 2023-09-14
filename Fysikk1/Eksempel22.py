#Side 51

import matplotlib.pyplot as plt

s = 0
v = 0
t = 0

s_slutt = 100
dt = 1E-3
s_verdier = []
v_verdier = []

def a(v):
    return -0.5*v + 6

while s < s_slutt:
    v += a(v)*dt
    s += v*dt
    s_verdier.append(s)
    v_verdier.append(v)

plt.plot(s_verdier, v_verdier)
plt.title("Fart som funksjon av posisjon")
plt.xlabel("Strekning")
plt.ylabel("Fart")
plt.grid()
plt.show()