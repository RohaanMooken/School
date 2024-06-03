def rekursiv(n):
    if n == 0:
        return 0
    else:
        return rekursiv(n-1) + n**3

print(rekursiv(50))


S = 1
n = 1

while n < 50:
    S = S + (n+1)**3
    n = n+1
    
print(n)
print(S)