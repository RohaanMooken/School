import pandas as pd 

import matplotlib.pyplot as plt 

df = pd.read_csv('frittfall.csv', sep=';', comment='#', decimal='.') 

tid = df['Tid'].tolist() 

fart = df['Fart'].tolist() 

posisjon=df['Posisjon'].tolist() 