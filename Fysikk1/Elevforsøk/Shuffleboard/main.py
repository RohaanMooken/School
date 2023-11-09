import math

def v_0(s, t):
    return 2 * s / t

def a(s, t, v0):
    return 2 * (s - v0 * t) / (t ** 2)

forsøk = []

masse = 0.314

# usikkerhet_masse = 0.01
# usikkerhet_strekning = 0.01
# usikkerhet_tid = 0.4

tid_liste = [2.35, 2.49, 2.40, 2.82, 2.45, 2.02, 2.17, 2.13, 1.60, 2.27]
strekning_liste = [3.79, 3.40, 3.72, 3.93, 2.22, 2.45, 2.13, 3.41, 2.14, 2.93]


# Trekke ifra 0.4 siden Evelyn ville
for i in range(10):
    tid_liste[i] = tid_liste[i] - 0.4
# Gjør dette i denne loopen fordi listen er oppdatert før vi starter på utregning

my_liste = []


for i in range(10):
    tid = tid_liste[i]
    strekning = strekning_liste[i]

    v0 = v_0(strekning, tid)
    akselerasjon = a(strekning, tid, v0)
    kraft = masse * akselerasjon
    friksjonskoeffisient = kraft / (9.81 * masse)
    my_liste.append(friksjonskoeffisient)

    # usikkerhet_kraft = kraft * math.sqrt((usikkerhet_masse/masse)**2 + (2*usikkerhet_tid/tid)**2)
    # usikkerhet_friksjonskoeffisient = math.sqrt((1/(9.81 * masse) * usikkerhet_kraft)**2 + (kraft/(9.81**2 * masse) * 0)**2)  

    forsøk.append([i, strekning, tid, v0, akselerasjon, f"{kraft:.2f} N", friksjonskoeffisient])

def tabell(experiments):
    print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Nr", "Strekning (m)", "Tid (s)", "Startfart (m/s)", "Akselerasjon", "Kraft (N)", "Friksjon (my)"))
    for experiment in experiments:
        print("{:<5} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f} {:<15} {:<15.2f}".format(*experiment))

tabell(forsøk)

# Fjern den største og den minste verdien
my_liste.remove(max(my_liste))
my_liste.remove(min(my_liste))

# Finner gjennomsnittet av my etter fjerning av ekstreme verdier
gjennomsnitt_my = sum(my_liste) / len(my_liste)

# Printer ut gjennomsnittet
print("\n\n",gjennomsnitt_my)
