amalie_lønn = 272.55
amaile_rente = 1.023

per_lønn = 272.55
per_rente = 1.0159

# Regne ut for Amalie
for i in range(17):
    amalie_lønn *= amaile_rente

# Per lønn i 2022
for i in range(14):
    per_lønn *= per_rente

    
print("I 2025 har Amalie en timelønnn på",round(amalie_lønn), "kr")
print("I 2022 har Per en timelønn på",round(per_lønn), "kr")

endring = (amalie_lønn-per_lønn)/per_lønn*100
print(round(endring, 2))