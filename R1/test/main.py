import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.ticker
plt.rcParams['figure.figsize'] = [14, 8]

df = pd.read_csv("C:\\Users\\danie\\GitHub\\School\\R1\\test\\test.csv", header=None, names=['Timestamp', 'Price', 'Volume'])

df['Date'] = pd.to_datetime(df['Timestamp'], unit='s')

df = df[df["Price"] > 0]
df = df.iloc[::-1]

def func(x, p1, p2):
    return p1 * np.log(x) + p2

ydata = np.log(df["Price"])
xdata = [x+1 for x in range(len(df))]

extended_dates = pd.date_range(df["Date"].iloc[0], "2023-01-01")

popt, pcov = curve_fit(func, xdata, ydata, p0=(3.0, -10))
print(popt)

fittedYdata = func(np.array([x+1 for x in range(len(df))]), popt[0], popt[1])
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