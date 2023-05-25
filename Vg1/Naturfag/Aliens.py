from random import randint

y = 1
forsøk = 100000
z = 0
nummer_av_generasjoner = 0
populasjon_cap = 50

for i in range(forsøk):
    for j in range(1000):
        for k in range(y):
            a = randint(1,4)
            if a == 1:
                y -= 1
            elif a == 2:
                break
            elif a == 3:
                y += 1
            else:
                y += 2
        if y <= 0:
            y = 1
            break
        if y >= populasjon_cap:
            nummer_av_generasjoner += j
            z += 1
            y = 1
            break
        
print(f"Survial probability: {round(z/forsøk, 3)*100} %")
print(f"Number of generations: {round(nummer_av_generasjoner/forsøk, 1)}")