import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the excel file into a pandas dataframe
data = pd.read_excel('Python/Resources/DData.xlsx')

x = np.linspace(0, 220)

def Ff(x, y, m, g):
    return np.arcsin(x/y)*m*g*np.cos(np.arcsin(x/y))

def Fc(friction_force, normal_force, theta, material):
    coef = abs(friction_force / (normal_force * np.cos(theta)))
    return np.where(coef < 0, 0, np.where(coef > 1, 1, coef))

fig, ax1 = plt.subplots()

for i, row in data.iterrows():
    y = row["y"]
    m = row["m"]
    g = row["g"]
    material = row["Material"]
    #ax1.plot(x, Fc(Ff(x, y, m, g), m*g, np.arcsin(x/y), material), label=material)
    ax1.plot(x, Ff(x, y, m, g), label=row["Material"])

ax1.set_xlabel("Height")
ax1.set_ylabel("Force of Friction")
ax1.tick_params('y', colors='b')
ax1.legend(loc='upper left')

plt.title('Force of Friction')
plt.show()
