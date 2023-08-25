a1 = float(input("Hva er a1? "))
a2 = float(input("Hva er a2? "))
an = float(input("Hva er an? "))

k = a2/a1

term = 1
sum = 0

while term < an:
    term *= k
    sum += term
    print(term)

print(f"\n{sum}")