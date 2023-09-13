import matplotlib.pyplot as plt

a = -10
s = 0
v = 50

posisjon = []
t = []
fart = []

dt = 0.01
tid = 0

while tid < 5:
    v += a * dt
    s += v * dt
    tid += dt
    t.append(tid)
    posisjon.append(s)
    fart.append(v)
    
plt.plot(t, posisjon)
plt.plot(t, fart)

plt.show()

