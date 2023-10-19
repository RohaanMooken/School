import matplotlib.pyplot as plt

'''
En person hopper ut fra fly
Ser bort fra luftmotstand

Lag et program som regner fartsgrafen til bevegelsen + posisjonsgraf
'''

def a(v): 
    sumkrefter=m*g-k*v**2 
    akselerasjon=sumkrefter/m 
    return akselerasjon 

m = 80
g = 9.81
dt = 0.01

s = 0
v = 0
t = 0

k = 0.3

t_verdier = []
s_verdier = []
v_verdier = []

t_verdier.append(t)
s_verdier.append(s)
v_verdier.append(v)

while t < 100:
    t = t + dt
    v = v + a(v) * dt
    s = s + v * dt
    t_verdier.append(t)
    s_verdier.append(s)
    v_verdier.append(v)


print(round(s, 2), round(t, 2))  
print("terminal", v)  
plt.plot(t_verdier, v_verdier)
plt.show()
plt.grid()    
