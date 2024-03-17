import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib

plt.rcParams['figure.figsize'] = [14, 8]

## load the data as a csv
df = pd.read_csv("C:\\Users\\danie\\Github\\School\\R1\\test\\BTC-USD.csv")

df.head()
#need to reverse the data later onddd
#remove entries where price is 0
df = df[df["High"] > 0]
df = df.iloc[::-1]
#convert Date to date format
df["Date"] = pd.to_datetime(df["Date"])
print(df.head())

#this is the function we want to fit over our data: a.log(x)+b
#we need to find appropriate coefficients
def func(x, p1, p2):
    return p1*np.log(x) + p2


#we are fitting log of price of BTC against the function, not actual price
ydata = np.log(df["High"])
xdata = [x+1 for x in range(len(df))] #just use numbers for dates

extended_dates = pd.date_range(df["Date"].iloc[0], "2023-01-01")

#extract optimal coefficients using curve fit
popt, pcov = curve_fit(func, xdata, ydata, p0=(3.0, -10))
#try to get ydata from xdata and function
#popt has coefficients, pcov has covariances between them
print(popt)

#generate fitted Y data
fittedYdata = func(np.array([x+1 for x in range(len(df))]), popt[0], popt[1])#pass values to function
fittedYdataExtended = func(np.array([x+1 for x in range(len(extended_dates))]), popt[0], popt[1])

plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.semilogy(df["Date"], df["High"])
ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())

# Configure minor ticks
ax.yaxis.set_minor_locator(ticker.LogLocator(base=10.0, subs=[1.0]))

plt.title("BTC log chart")
plt.ylabel("Price in USD")
plt.show()

plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.semilogy(df["Date"], df["Closing Price (USD)"])
plt.yscale('log', subsy=[1])
ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(matplotlib.ticker.ScalarFormatter())
plt.plot(df["Date"], np.exp(fittedYdata))

plt.title("BTC logarithmic regression")
plt.ylabel("Price in USD")
plt.ylim(bottom=0.1)
plt.show()



#####################
from sklearn.linear_model import LinearRegression
def get_furthest_x(y, line):
    #y is all the log of values 
    # line is the linear regression line
    difference = [abs(y[x] - line[x]) for x in range(len(line))]
    max_difference = max(difference)
    return difference.index(max_difference)

df["ind"] = [x+1 for x in range(len(df))]
#df = df[df.Date >= "2010-09-16"]
def perform_regression(df):
    X = np.array(np.log(df.ind)).reshape(-1,1) #makes it a list of lists incase we had multiple linear regression
    y = np.array(np.log(df.Value))

    #now X and y are how they look on a log-log chart
    reg = LinearRegression().fit(X,y)

    #remember plt plots on a linear axis and our X and y have been "logged"
    #plt.plot((X), (reg.predict(X))) #plot the X and predicted y as per X
    line = reg.predict(X)
    outlier = get_furthest_x(y, line) #index of furthest element from line
    return outlier
df2 = df
iterations = int(len(df2)/2)
print(iterations)
for i in range(0,iterations):
    outlier = perform_regression(df2)
    #outlier is the xth index from beginning, we need to drop it
    df2=df2.drop(df2.index[outlier])
    
#now we have df2, perform linear regression and get the line for it
X = np.array(np.log(df2.ind)).reshape(-1,1) #makes it a list of lists incase we had multiple linear regression
y = np.array(np.log(df2.Value))

#now X and y are how they look on a log-log chart
reg = LinearRegression().fit(X,y)

#remember plt plots on a linear axis and our X and y have been "logged"
#plt.plot((X), (reg.predict(X))) #plot the X and predicted y as per X
line = reg.predict(X)
#we want correlation between line and X

r = np.corrcoef(np.log(df2.Value), line)
print(r)
