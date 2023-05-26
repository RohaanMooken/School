n = int(input("Klosser: "))
a = 0
m = 1

while a <= n:
    a += m**2
    m += 1
    print(a)

if a > n:
    print(m-1)
else:
    print(m)