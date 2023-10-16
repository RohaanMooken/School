'''
Her er ett program der du kan sette inn et funksjonsutrykk og finne vekstfarten

Du trenger:

- f(x)
- x
- dx
'''

def f(x):
    return funksjonsutrykk


def deriverte(f, x, dx):
    deriverte = (f(x+dx) - f(x-dx)) / (2*dx)
    return round(deriverte, 6)

    
funksjonsutrykk = input("f(x): ")
f = lambda x: eval(funksjonsutrykk)

x = float(input("x: "))
dx = float(input("dx: "))

print(deriverte(f, x, dx))

