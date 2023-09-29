def f(x): 
    return x**3 + 2*x**2 + 3*x - 6

svar = input("Velg verdi for a: ") 
a = float(svar) 

t = 0.1 
while t > 0.0000001: 
    print("f(" + str(round(a - t, 7)) + ") =", round(f(a - t), 7)) 
    t = t/10 

t = 0.1 
while t > 0.0000001: 
    print("f(" + str(round(a + t, 7)) + ") =", round(f(a + t), 7)) 
    t = t/10 