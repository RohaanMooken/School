"""
Når det er mer enn 1 trinn igjen, tar kaninen to mulige valg: å hoppe ett trinn eller to trinn. 
For hvert av disse valgene, blir funksjonen kalt rekursivt for å finne ut antall måter å hoppe de gjenværende trinnene. 
Til slutt legger funksjonen sammen disse to resultatene for å gi det totale antall måter kaninen kan hoppe opp n trinn.
"""

# n er trinn
def trapp(n):
    # Bare en måte å komme opp, derfor bare en måte (0 er 2 i dette tilfellet med at det går opp)
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        # Returnerte antall måter kaninen kan hoppe opp med 
        return trapp(n - 1) + trapp(n - 2) + trapp(n - 3)
    
trinn = 10
måter = trapp(trinn)

print(f"{måter}")

"""
trapp(n=4): Funksjonen trapp(4)
to rekursive kall: trapp(3) og trapp(2), fordi kaninen kan hoppe ett trinn eller to trinn fra nåværende posisjon.

trapp(2) er resultatet av trapp(1) + trapp(0), altså 1 + 1 = 2. 
trapp(3) er resultatet av trapp(2) + trapp(1), altså 2 + 1 = 3. 
trapp(4) er resultatet av trapp(3) + trapp(2), altså 3 + 2 = 5.
"""