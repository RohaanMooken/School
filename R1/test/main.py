import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.ticker
plt.rcParams['figure.figsize'] = [14, 8]

df = pd.read_csv("C:\\Users\\danie\\GitHub\\School\\R1\\test\\test.csv", header=None, names=['Timestamp', 'Price', 'Volume'])

df['Date'] = pd.to_datetime(df['Timestamp'], unit='s')

# Fjerner rader hvor prisen er 0 eller negativ
df = df[df["Price"] > 0]

# Inverterer dataframe slik at den nyeste raden kommer først
df = df.iloc[::-1]

# Definerer en funksjon som beregner en verdi basert på logaritmen av x, skalert med p1, og justert med p2
def func(x, p1, p2):
    return p1 * np.log(x) + p2

# Beregner den naturlige logaritmen til alle prisene for bruk i kurvetilpasningen
ydata = np.log(df["Price"])

# Oppretter en liste med sekvensielle tall startende fra 1, tilsvarende lengden på dataframe
xdata = [x+1 for x in range(len(df))]

# Lager en utvidet dato rekkevidde fra første dato i dataframe til 1. januar 2023
extended_dates = pd.date_range(df["Date"].iloc[0], "2023-01-01")

# Bruker kurvetilpasning for å finne optimale parametere (p1, p2) for vår funksjon basert på xdata og ydata, starter gjetting med p0
popt, pcov = curve_fit(func, xdata, ydata, p0=(3.0, -10))

# Skriver ut de optimale parameterne funnet av kurvetilpasningen
print(popt)

# Beregner tilpassede y-verdier basert på den opprinnelige datoen ved hjelp av de optimale parameterne
fittedYdata = func(np.array([x+1 for x in range(len(df))]), popt[0], popt[1])

# Beregner tilpassede y-verdier for den utvidede dato rekkevidden basert på de optimale parameterne
fittedYdataExtended = func(np.array([x+1 for x in range(len(extended_dates))]), popt[0], popt[1])


plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.semilogy(df["Date"], df["Price"])
plt.yscale('log')
ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(matplotlib.ticker.ScalarFormatter())
plt.plot(df["Date"], np.exp(fittedYdata))

plt.title("BTC logarithmic regression")
plt.ylabel("Price in USD")
plt.ylim(bottom=0.1)
plt.show()