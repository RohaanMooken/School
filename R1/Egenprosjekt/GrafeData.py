import pandas as pd
import matplotlib.pyplot as plt

# Erstatt 'din_fil.csv' med den faktiske filbanen til din CSV-fil
csv_fil = 'data.csv'  # Husk å endre denne til riktig filbane

# Les inn CSV-filen
data = pd.read_csv(csv_fil)

# Grupper dataene etter 'date' og summer 'cases'
daglig_sum = data.groupby('date')['cases'].sum().reset_index()

# Plot resultatene
plt.figure(figsize=(10, 6))
plt.plot(daglig_sum['date'], daglig_sum['cases'], marker='o', linestyle='-')
plt.title('Antall smittede av COVID-19 per dag')
plt.xlabel('Dato')
plt.ylabel('Antall smittede')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
