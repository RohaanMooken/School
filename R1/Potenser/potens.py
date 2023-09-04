
def potens(grunntall, potens):
    resultat = 1
    for i in range(1, potens + 1):
        resultat *= grunntall
    return resultat

for i in range(5):
    print(potens(i, 2))