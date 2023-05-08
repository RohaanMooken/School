import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_excel("Resources/data.xlsx")

x, y1, y2 = [], [], []

for i, row in file.iterrows():
    if i == 0:
        pass
    x.append(row["Day"])
    y1.append(row["Population"])
    y2.append(row["Cases"])

plt.plot(x, y1)
plt.plot(x, y2)
plt.legend()
plt.show()