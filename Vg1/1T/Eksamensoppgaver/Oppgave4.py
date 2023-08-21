def f(x):
    return 1/9 * (x + 1) * (x - 6) ** 2  # Definerer funksjonen f

x_min = 0  # Minste x-verdi
x_max = 6  # Største x-verdi

n = 6000  # Antall rektangler

bredde = (x_max - x_min) / n  # Bredden av hvert rektangel

def tilnærmet_areal(f, x_min, x_max, n):
    totalt_areal = 0
    x = x_min
    for i in range(n):
        totalt_areal += f(x) * bredde
        x += bredde

        #print(x, "=", totalt_areal)
    return totalt_areal

areal = tilnærmet_areal(f, x_min, x_max, n)
#print("\nTilnærmet areal:", round(areal, 3), "cm^2")
print("\nTilnærmet areal:", areal, "cm^2")
