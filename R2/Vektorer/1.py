import math
import numpy as np

bool = input("Har du en vektor? ")

if bool:
    a = int(input("Hva er a verdien i vektoren? "))
    b = int(input("Hva er b verdien i vektoren? "))
    c = int(input("Hva er c verdien i vektoren? "))

    lengde = math.sqrt(a**2 + b**2 + c**2)
else:
    p1A = int(input("Hva er A verdien til punkt 1? "))
    p1B = int(input("Hva er B verdien til punkt 1? "))
    p1C = int(input("Hva er C verdien til punkt 1? "))
    p2A = int(input("Hva er A verdien til punkt 2? "))
    p2B = int(input("Hva er B verdien til punkt 2? "))
    p2C = int(input("Hva er C verdien til punkt 2? "))

    p1p2 = np.array([p2A - p1A, p2B - p1B, p2C - p1C])

    lengde = math.sqrt(p1p2[0]**2 + p1p2[1]**2 + p1p2[2]**2)

print(f"Lengden til vektoren er {round(lengde, 2)}")