import numpy as np
import matplotlib.pyplot as plt

# Konstanter
m = 0.4  # kg
theta = np.radians(30)  # grader
g = 9.81  # m/s^2
my = 0.35  # friksjonskoeffisient

dt = 0.001

# startbetingelser
s = 0
v = 3.2  # m/s
t = 0

# Konstante krefter
Gx = m * g * np.sin(theta)
Gy = m * g * np.cos(theta)
N = Gy

def a(v):
    R = -np.sign(v) * my * N
    sum_F = -Gx + R
    aks = sum_F / m
    return aks

# lister for å lagre data
t_list = [t]
v_list = [v]
s_list = [s]

while s >= 0:
    v += a(v) * dt
    s += v * dt
    t += dt

    t_list.append(t)
    v_list.append(v)
    s_list.append(s)

    print(f"Time: {t:.3f} s, Velocity: {v:.3f} m/s, Position: {s:.3f} m")

plt.plot(t_list, v_list)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)
plt.show()