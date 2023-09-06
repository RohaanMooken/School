import matplotlib.pyplot as plt
import numpy as np

# Legg inn resultatene fra forsøkene for hvert lag
lag_navn = ["Lag 1", "Lag 2", "Lag 3", "Lag 4", "Lag 5", "Lag 6", "Lag 7"]

resultater_gulv = [
    [53, 70, 91],  # Lag 1
    [25, 39, 147],  # Lag 2
    [51, 62, 102],  # Lag 3
    [53, 52, 87],  # Lag 4
    [55, 0, 144],  # Lag 5
    [28, 20, 20],  # Lag 6
    [72, 117, 148],  # Lag 7
]

resultater_hjul = [
    [507, 774, 716],  # Lag 1
    [300, 432, 527],  # Lag 2
    [341, 455, 500],  # Lag 3
    [195, 0, 230],  # Lag 4
    [0, 0, 562],  # Lag 5
    [0, 0, 0],  # Lag 6
    [0, 0, 0],  # Lag 7
]

# X-verdier for alle grafene
x_values = np.arange(len(lag_navn))

# Bredde for søylene
bar_width = 0.35

# Opprett en figur og aksene for grafene
fig, axs = plt.subplots(1, 1, figsize=(12, 6))

# Loop gjennom hvert lag og lag horisontale søylediagrammer for forsøkene på gulv
for i in range(len(lag_navn)):
    axs.barh(x_values + i * bar_width, resultater_gulv[i], bar_width, label=lag_navn[i] + ' (Gulv)')

# Loop gjennom hvert lag og legg til horisontale søylediagrammer for forsøkene på hjul under hver
for i in range(len(lag_navn)):
    hjul_data = [0 if val == 0 else -val for val in resultater_hjul[i]]  # Konverter nullverdier til negative
    axs.barh(x_values + i * bar_width, hjul_data, bar_width, label=lag_navn[i] + ' (Hjul)')

axs.set_yticks(x_values)
axs.set_yticklabels(lag_navn)
axs.set_xlabel('Resultat')
axs.set_title('Sammenligning av forsøk på gulv og hjul')

# Juster layouten for å unngå overlappende tekster
plt.tight_layout()

# Vis grafene
plt.legend()
plt.show()
