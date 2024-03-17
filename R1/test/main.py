import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.linear_model import LinearRegression

plt.rcParams['figure.figsize'] = [14, 8]

# Load the data from CSV
# Assuming the CSV has no header, we specify column names directly
df = pd.read_csv("C:\\Users\\danie\\GitHub\\School\\R1\\test\\btc.csv", header=None, names=['Timestamp', 'Price', 'Volume'])

# Convert Timestamp to datetime format (assuming Timestamp is in Unix time)
df['Date'] = pd.to_datetime(df['Timestamp'], unit='s')

# We'll use 'Price' as 'High' for consistency with your original script
df['High'] = df['Price']

# Reverse the data order and filter out entries with Price <= 0
df = df[df["High"] > 0]
df = df.iloc[::-1]

print(df.head())

# Define the model function to fit over our data
def func(x, p1, p2):
    return p1 * np.log(x) + p2

# Prepare data for curve fitting
ydata = np.log(df["High"])
xdata = np.array([x+1 for x in range(len(df))])  # Use sequential numbers for x

# Extract optimal coefficients using curve fit
popt, pcov = curve_fit(func, xdata, ydata, p0=(3.0, -10))
print(popt)

# Generate fitted Y data
fittedYdata = func(xdata, *popt)

# Plotting
plt.style.use("dark_background")

fig, ax = plt.subplots()
ax.semilogy(df["Date"], df["High"].values)  # Original data
plt.plot(df["Date"], np.exp(fittedYdata), label="Fitted curve")  # Fitted curve
ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
plt.title("BTC Price Logarithmic Fit")
plt.ylabel("Price in USD")
plt.legend()
plt.show()

# Regression analysis part
df["ind"] = [x+1 for x in range(len(df))]

def perform_regression(df):
    X = np.log(df["ind"].values).reshape(-1, 1)  # Convert index to numpy array and log
    y = np.log(df["High"].values)  # Convert price to numpy array and log
    reg = LinearRegression().fit(X, y)
    line = reg.predict(X)
    difference = np.abs(y - line)
    max_difference = np.max(difference)
    return np.argmax(difference)

df2 = df.copy()
iterations = int(len(df2)/2)
print(iterations)

for i in range(iterations):
    outlier = perform_regression(df2)
    df2 = df2.drop(df2.index[outlier])

# Perform linear regression on the cleaned dataset
X = np.log(df2["ind"].values).reshape(-1, 1)
y = np.log(df2["High"].values)
reg = LinearRegression().fit(X, y)
line = reg.predict(X)

# Calculate and print the correlation coefficient
r = np.corrcoef(y, line)[0, 1]
print(f"Correlation coefficient: {r}")
