def P(x):
    y = x**3 + 3*x**2 - x - 3
    return y

for i in range(-10, 11):
    if P(i) == 0:
        if i < 0:
            print("En faktor er x +", abs(i))
        elif i == 0:
            print("En faktor er x")
        else:
            print("Siste faktor er x -", i)