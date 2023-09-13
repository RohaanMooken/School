import matplotlib.pyplot as plt

def ask(v):
    return a - 1*v
a = 10
v = 0
s = 0

posisjon = []
t = []
fart = []

dt = 0.01
tid = 0

while tid < 5:
    v += ask(v) * dt
    s += v * dt
    tid += dt
    t.append(tid)
    posisjon.append(s)
    fart.append(v)
    
plt.plot(t, fart)

plt.show()

