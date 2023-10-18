import matplotlib.pyplot as plt

'''
En person hopper ut fra fly
Ser bort fra luftmotstand

Lag et program som regner fartsgrafen til bevegelsen + posisjonsgraf
'''

m = 80
g = 9.81

s = 0
v = 0
t = 0
dt = 0.01

t_verdier = []
s_verdier = []
v_verdier = []

t_verdier.append(t)
s_verdier.append(s)
v_verdier.append(v)

while v < 30:
    t = t + dt
    v = v + g * dt
    s = s + v * dt
    t_verdier.append(t)
    s_verdier.append(s)
    v_verdier.append(v)


print(round(s, 2), round(t, 2))    
plt.plot(t_verdier, s_verdier)
plt.show()
plt.grid()    
