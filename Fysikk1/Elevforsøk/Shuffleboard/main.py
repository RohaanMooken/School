import math

def v_0(s, t):
    return 2 * s / t

def a(s, t, v0):
    return 2 * (s - v0 * t) / (t ** 2)

forsøk = []

masse = 0.314

usikkerhet_masse = 0.01  # Eksempel på usikkerhet i masse
usikkerhet_strekning = 0.01  # Eksempel på usikkerhet i strekning
usikkerhet_tid = 0.4  # Eksempel på usikkerhet i tid

tid_liste = [2.35, 2.49, 2.40, 2.82, 2.45, 2.02, 2.17, 2.13, 1.60, 2.27]
strekning_liste = [3.79, 3.40, 3.72, 3.93, 2.22, 2.45, 2.13, 3.41, 2.14, 2.93]


for i in range(10):
    tid = tid_liste[i]
    strekning = strekning_liste[i]

    # Beregner startfart
    v0 = v_0(strekning, tid)

    # Beregner akselerasjon
    akselerasjon = a(strekning, tid, v0)

    # Beregner kraft (R = m * a)
    kraft = masse * akselerasjon

    # Beregner friksjonskoeffisient (my = R/N, antar N er konstant)
    friksjonskoeffisient = kraft / (9.81 * masse)

    # Beregner usikkerhet i kraft (ΔR = m*a*sqrt((Δm/m)^2 + (Δa/a)^2))
    usikkerhet_kraft = kraft * math.sqrt((usikkerhet_masse/masse)**2 + (2*usikkerhet_tid/tid)**2)

    # Beregner usikkerhet i friksjonskoeffisient (Δmy = sqrt((1/N * ΔR)^2 + (R/N^2 * ΔN)^2))
    usikkerhet_friksjonskoeffisient = math.sqrt((1/(9.81 * masse) * usikkerhet_kraft)**2 + (kraft/(9.81**2 * masse) * 0)**2)  

    forsøk.append([i, strekning, tid, akselerasjon, f"{kraft:.2f} N", friksjonskoeffisient, usikkerhet_friksjonskoeffisient])


# Skriver ut tabellen
def tabell(experiments):
    print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Nr", "Strekning (m)", "Tid (s)", "Akselerasjon", "Kraft (N)", "Friksjon (my)", "Usikkerhet my"))
    for experiment in experiments:
        print("{:<5} {:<15.2f} {:<15.2f} {:<15.2f} {:<15} {:<15.2f} {:<15.2f}".format(*experiment))


# Simulerer eksperimenter og skriver ut tabellen
tabell(forsøk)
