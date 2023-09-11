x = 10000

def logaritme(x, n=10):
    svar = 0
    while x >= n:
        x /= n
        svar += 1
        
    return svar

verdi = logaritme(x)
print(verdi)
