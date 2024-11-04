# Sette index: 0
n = 643 - 2

def main(n):
    tall = [1, 3, 5, 7]
    
    # Base 4
    base = len(tall)
    
    result = []
    for i in range(5):
        # I hver iterasjon beregner vi resten av n når det divideres med basen (4 i dette tilfellet) ved å bruke 'n % base'.
        # n % base
        
        # Denne operasjonen gir oss indeksen for å få tilgang til den tilsvarende verdien i tall-listen.
        # tall[n % base]
        
        # Tall listen inneholder de spesifikke verdiene vi ønsker skal representere tallet vårt i base-4.
            
        # Ved å bruke 'tall[n % base]', kartlegger vi resten til riktig verdi i 'tall'.
        result.insert(0, tall[n % base]) # 'result.insert(0, ...)' legger bare til denne verdien i starten av listen
        
        # Etter å ha satt inn verdien, oppdaterer vi n ved å utføre en heltallsdivisjon med basen ved å bruke 'n //= base'.
        n //= base
    return result

# Utregning:
# Koden konverterer tallet n (641) til en base-4-representasjon ved å bruke verdiene i tall-listen.
# Hver iterasjon trekker ut en tall i base 4 og tilordner den til en tilsvarende verdi i 'tall'.

# n = 641

# 1:
#   tall = 641 % 4 = 1
#   tall[1] = 3
#   result = [3]
#   
#   Neste tall:
#   n = 641 // 4 = 160

# 2:
#   tall = 160 % 4 = 0
#   tall[0] = 1
#   result = [1, 3]
#   
#   Neste tall:
#   n = 160 // 4 = 40

# 3:
#   tall = 40 % 4 = 0
#   tall[0] = 1
#   result = [1, 1, 3]
# 
#   Neste tall
#   n = 40 // 4 = 10

# 4:
#   tall = 10 % 4 = 2  
#   tall[2] = 5
#   result = [5, 1, 1, 3]
#   
# Neste tall:   
#   n = 10 // 4 = 2

# 5:
#   tall = 2 % 4 = 2  
#   tall[2] = 5
#   result = [5, 5, 1, 1, 3]
#   
#   Treffer 0 og vi er ferdig
#   n = 2 // 4 = 0

# [5, 5, 1, 1, 3]
print(main(n))
# 55113
print(''.join(map(str, main(n))))