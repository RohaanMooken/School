import matplotlib.pyplot as plt

def a(v): 
    sumkrefter = -my * m * g - k * v**2
    akselerasjon = sumkrefter/m
    return akselerasjon

m = 800
g = 9.81
dt = 0.01
my = 0.7 


t = 0
v = 120/3.6
s = 0

t_verdier = []
s_verdier = []
v_verdier = []

k = 0.47

t_verdier.append(t)
s_verdier.append(s)
v_verdier.append(v)

while v >= 0:
    t = t + dt
    v = v + a(v) * dt
    s = s + v * dt
    t_verdier.append(t)
    s_verdier.append(s)
    v_verdier.append(v)


print("Bremselengde med luftmotstand", s)
# plt.plot(t_verdier, s_verdier)
# plt.show()
# plt.grid()    
