from sympy import * # bibliotek som håndterer likninger 
import matplotlib.pylab as plt

S = 340 # mottatt solstråling 
alfa = 0.1 # albedo fra figur i kapittel 6C 
sigma = 5.67e-8 

# Definerer variablene i likningene 
# T_0 på jordoverflaten, K 
# T_1 i atmosfæren, K 
T_0, T_1 = symbols('T_0, T_1', nonnegative = True) 

x_list = [] # albedo
y_list = [] # resultatet

while alfa < 1:
    # Definerer venstre og høyre side i strålingsbalansen på jordoverflaten 
    inn_jord = (S + sigma*T_1**4) 
    ut_jord = (sigma*T_0**4 + alfa*S) 

    # Definerer venstre og høyre side i strålingsbalansen i atmosfæren 
    inn_atmosfare = (sigma*T_0**4) 
    ut_atmosfare = (2*sigma*T_1**4)

    # Definerer likningene 
    l1 = Eq(inn_jord , ut_jord) 
    l2 = Eq(inn_atmosfare , ut_atmosfare) 

    # Løser likningssettet 
    T = solve([l1, l2]) 
    
    # Tar utgangspunkt i jordoverflate
    verdi = (T[0][T_0])
    
    x_list.append(alfa)
    y_list.append(verdi)    
    alfa += 0.01

plt.plot(x_list, y_list)
plt.xlabel("Albedo")
plt.ylabel("Temperaturen på jordoverflaten")
plt.grid()
plt.show()