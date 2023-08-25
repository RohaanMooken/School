term = 1
sum = 0

while sum <= 19683:
    print(sum)
    sum += term
    term *= 3
    
print(sum)