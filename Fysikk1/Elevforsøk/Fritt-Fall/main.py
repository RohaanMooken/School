import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('frittfall.csv', sep=';', comment='#', decimal='.')

tid = df['Tid'].tolist()
posisjon = df['Posisjon'].tolist()
fart = df['Fart'].tolist()

g = 9.8 

masse = 0.5
potensiell_energi = [masse * g * i for i in posisjon]
kinetisk_energi = [(1/2) * masse * v**2 for v in fart]
mekanisk_energi = [potensiell + kinetisk for potensiell, kinetisk in zip(potensiell_energi, kinetisk_energi)]

plt.figure(figsize=(10, 6))

plt.plot(tid, potensiell_energi, label='Potensiell energi')
plt.plot(tid, kinetisk_energi, label='Kinetisk energi')
plt.plot(tid, mekanisk_energi, label='Mekanisk energi')

plt.xlabel('Tid (s)')
plt.ylabel('Energi (Joule)')
plt.title('Energi vs. Tid')
# plt.legend()
plt.grid(True)
plt.show()
