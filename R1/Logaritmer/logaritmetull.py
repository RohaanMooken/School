x = 10000

def logaritme(x):
    svar = 0
    for i in str(x):
        if i == '1':
            continue
        else: 
            svar += 1
            
    return svar

verdi = logaritme(x)
print(verdi)
