n = int(input("Klosser: "))
a = 0
m = 1

while a <= n:
    a += m**2
    m += 1

if a > n:
    print(f"Antall figurer: {m-1}")
else:
    print(f"Antall figurer: {m}")