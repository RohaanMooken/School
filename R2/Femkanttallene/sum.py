n = int(input("Antall femkant: "))

sum = 0

def pentagon(n):
    if n == 1:
        return 1
    elif n == 2:
        return 5
    return pentagon(n - 1) + (n * 2) + (n - 2)

for i in range(1, n + 1):
    sum += pentagon(i)

print(f"Summen av de første {n} femkantene er {sum}")