def f(x):
    return 1 / 9 * (x + 1) * (x - 6)**2

x_min = 0
x_maks = 6
n = 6000
sum = 0
i = 0

bredde = (x_maks - x_min) / n

for j in range(n):
    sum += bredde * f(i)
    i += bredde

print(f"Areal: {sum}")