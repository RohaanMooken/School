# Drivhuseffekt med likevekt slik 

# den er fremstilt i boka i kapittel 7D 

from sympy import * # bibliotek som håndterer likninger 

# konstanter 

S = 340 # mottatt solstråling 

alfa = 0.1 # albedo fra figur i kapittel 6C 

sigma = 5.67e-8 
# konstanten i stefan-boltzmannslov 

# Definerer variablene i likningene 

# T_0 på jordoverflaten, K 

# T_1 i atmosfæren, K 

T_0, T_1 = symbols('T_0, T_1', nonnegative = True) 

# Definerer venstre og høyre side 

# i strålingsbalansen på jordoverflaten 

inn_jord = (S + sigma*T_1**4) 
ut_jord = (sigma*T_0**4 + alfa*S) 

# Definerer venstre og høyre side 
# i strålingsbalansen i atmosfæren 

inn_atmosfare = (sigma*T_0**4) 

ut_atmosfare = (2*sigma*T_1**4)
# Definerer likningene 

# inn_jord = ut_jord 

# inn_atmosfære = ut_atmosfære 

l1 = Eq(inn_jord , ut_jord) 

l2 = Eq(inn_atmosfare , ut_atmosfare) 

# Løser likningssettet 

T = solve([l1, l2]) 

#  

# Skriver ut løsningen 

print("Temperaturen på jordoverflaten T_0 =", T[0][T_0], "K.") 

print("Temperaturen i atmosfæren T_1 =", T[0][T_1], "K.") 