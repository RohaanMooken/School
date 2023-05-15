import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# read the excel file into a pandas dataframe
data = pd.read_excel('Resources/data.xlsx')

# extract the x and y variables from the dataframe
x_data = data['Day']
y_data = data['Cases']

# Define logistic function
def logistic_func(x, a, b, c, d):
    return a / (1 + np.exp(-c * (x - d))) + b

# Define derived function for the logistic function
def d_logistic_func(x, a, b, c, d):
    return (a * c * np.exp(-c * (x - d))) / (1 + np.exp(-c * (x - d)))**2

# Fit logistic function to data
popt, pcov = curve_fit(logistic_func, x_data, y_data)

dx = 1E-9

def derivert(x):
    return (d_logistic_func(x+dx, *popt)-d_logistic_func(x, *popt))/dx

################################################################
fig, ax0 = plt.subplots()
ax0.plot(x_data, y_data, 'bo', label='Data')
ax0.set_xlabel("Dager")
ax0.set_ylabel("Antall Smittet")

# Create a new figure with two y-axes
fig, ax1 = plt.subplots()

# Plot data and logistic function on first y-axis
ax1.plot(x_data, logistic_func(x_data, *popt), 'r-', label='Logistic Function')
ax1.set_xlabel("Dager")
ax1.set_ylabel("Antall Smittet")
ax1.tick_params('y', colors='b')
ax1.legend(loc='upper left')

# Create second y-axis for the derived function
# ax2 = ax1.twinx()
fig, ax2 = plt.subplots()

# Plot derived function on second y-axis
ax2.plot(x_data, d_logistic_func(x_data, *popt), 'g-', label='Derived Function')
ax2.set_xlabel("Dager")
ax2.set_ylabel("Antall Smittet")
ax2.tick_params('y', colors='g')
ax2.legend(loc='upper right')

# Plot derived of the derived function on second y-axis
# ax3 = ax2.twinx()
fig, ax3 = plt.subplots()

ax3.plot(x_data, derivert(x_data), 'm-', label='Double Derived Function')
ax3.set_xlabel("Dager")
ax3.set_ylabel("Antall Smittet")
ax3.tick_params('y', colors='m')
ax3.legend(loc='lower right')

#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################

nullpunkter, ekstremalpunkter, vendepunkter = [], [], []

def f(x):
    return logistic_func(x, *popt)

def df(x):
    return d_logistic_func(x, *popt)

def ddf(x):
    return derivert(x)

def samesign(a, b):
        return a * b > 0

def rrd(List):
    return list(dict.fromkeys([round(x, 2) for x in List]))

def bisect(f, a, b):
    
    assert not samesign(f(a), f(b)), "[ERROR] a and b variables are of the same sign"

    for i in range(54):
        c = (a+b)/2
        if samesign(f(a), f(c)):
            a = c
        else:
            b = c

    return c

# def newton(f, df, x0, tol=1e-6):
#     if abs(f(x0)) < tol:
#         return x0
#     else:
#         return newton(f, df, x0 - f(x0)/df(x0), tol)

a = int(x_data[0])
b = int(x_data[len(x_data)-1])

for i in range(a-10, a):
    vendepunkter.append(bisect(ddf, i, b))

# for i in range(500, 700):
#     # nullpunkter.append(newton(f, df, i))
#     ekstremalpunkter.append(newton(df, ddf, i))

# ekstremalpunkter.append(100)
# for i in range(a, b):
#     for j in range(len(ekstremalpunkter)):
#         if abs(df(i)) < ekstremalpunkter[j]:
#             ekstremalpunkter[j] = df(i)


nullpunkter = rrd(nullpunkter)
ekstremalpunkter = rrd(ekstremalpunkter)
vendepunkter = rrd(vendepunkter)

# print(nullpunkter)
# print(ekstremalpunkter)
# print(vendepunkter)

#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################

# # Plot roots on first y-axis
# ax1.plot(roots_real, logistic_func(roots_real, *popt), 'bs', label='Roots')

# # Plot extrema on first y-axis
# ax2.plot(extrema_x, d_logistic_func(extrema_x, *popt), 'go', label='Extrema')

# # Plot turning points on first y-axis
for x in vendepunkter:
    ax3.plot(x, ddf(x), 'm^', label='Turning Points')
    ax2.plot(x, df(x), 'g^', label='Extremum Points')
    ax1.plot(x, f(x), 'r^', label='Turning Points')


plt.title('Logistic Function with Derived Function')
plt.show()
