import matplotlib.pyplot as plt
import numpy as np

# Toppunkt, Bunnpunkt, monotoniegenskaper, krumning og vendepunkt

a = -4
b = 2
h = 0.00001

nullpunkter, vendepunkter, ekstremalpunkter = [], [], []
Nullpunkter, Vendepunkter, Ekstremalpunkter= [], [], []

def f(x):
    return x**3+3.9*x**2+0.5*x-2.7

def Df(x):
    return (f(x+h)-f(x))/h

def DDf(x):
    return (Df(x+h)-Df(x))/h

def pp(x, y, color = str):
    plt.plot(x, y, marker=".", markersize=10, markerfacecolor=color)

def ko():
    print("-_-", end=" ")

def kn():
    print("_-_", end=" ")

def samesign(a, b):
        return a * b > 0

def rrd(List):
    return list(dict.fromkeys([round(x, 5) for x in List]))

def bisect(f, a, b):
    
    assert not samesign(f(a), f(b)), "[ERROR] a and b variables are of the same sign"

    for i in range(54):
        c = (a+b)/2
        if samesign(f(a), f(c)):
            a = c
        else:
            b = c

    return c

def newton(f, df, x0, tol=1e-6):
    # output is an estimation of the root of f 
    # using the Newton Raphson method
    # recursive implementation
    if abs(f(x0)) < tol:
        return x0
    else:
        return newton(f, df, x0 - f(x0)/df(x0), tol)

x = np.linspace(a, b, 1000)

for i in range(a-10, a):
    Vendepunkter.append(bisect(DDf, i, b))

for i in range(a, b):
    Nullpunkter.append(newton(f, Df, i, tol=1e-6))
    Ekstremalpunkter.append(newton(Df, DDf, i, tol=1e-6))

nullpunkter = rrd(Nullpunkter)
ekstremalpunkter = rrd(Ekstremalpunkter)
vendepunkter = rrd(Vendepunkter)
# print(nullpunkter)
# print(ekstremalpunkter)
# print(vendepunkter)

plt.plot(x, f(x), label="f(x)")
plt.plot(x, Df(x), label="f'(x)")
plt.plot(x, DDf(x), label="f''(x)")

for nullpunkt in nullpunkter:
    pp(nullpunkt, f(nullpunkt), "blue")

print("----------------------------------------")
print("Monotoniegenskaper:")

for ekspunkt in ekstremalpunkter:
    if DDf(ekspunkt) > 0:
        pp(ekspunkt, f(ekspunkt), "green")
    else:
        pp(ekspunkt, f(ekspunkt), "red")
    if ekspunkt == ekstremalpunkter[len(ekstremalpunkter)-1]:
        if Df(ekspunkt-1) > 0:
            print("---", end=" 0 ")
        else:
            print("- - -", end=" 0 ")
        if Df(ekspunkt+1) < 0:
            print("- - -")
        else:
            print("---")
    else:
        if Df(ekspunkt-1) > 0:
            print("---",end=" 0 ")
        else:
            print("- - -",end=" 0 ")

print("----------------------------------------")
print("Krumning til grafen:")

for vendepunkt in vendepunkter:
    pp(vendepunkt, f(vendepunkt), "yellow")
    # Sjekk for kruming
    if vendepunkt == vendepunkter[len(vendepunkter)-1]:
        # Sjekk krumning venstre og høyre for punktet
        if DDf(vendepunkt-1) > 0:
            ko()
            print("0", end=" ")
        else:
            kn()
            print("0", end=" ")
        if DDf(vendepunkt+1) < 0:
            kn()
        else:
            ko()
    else:
        # Sjekk kruming til venstre
        if DDf(vendepunkt-1) > 0:
            ko()
            print("0")
        else:
            kn()
            print("0")

print("\n----------------------------------------")

plt.legend()
plt.grid()
plt.show()
