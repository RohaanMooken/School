def base_eksponent(funksjonsutrykk):
    funksjonsutrykk = funksjonsutrykk.replace("^", "**").replace(" ", "")
    
    if '**' in funksjonsutrykk:
        operator_pos = funksjonsutrykk.index('**')
    elif '^' in funksjonsutrykk:
        operator_pos = funksjonsutrykk.index('^')
    
    base = funksjonsutrykk[:operator_pos]
    eksponent = funksjonsutrykk[operator_pos + 2:]
    
    if not eksponent:
        eksponent = 1
    
    # Se om basen inneholder et tall
    num_in_base = ""
    for char in base:
        if char.isdigit():
            num_in_base += char
        else:
            break
    base = 'x'
    return base, eksponent, num_in_base

# Be brukeren om å skrive inn funksjonsuttrykk
funksjonsutrykk = input("Skriv inn funksjonsuttrykk (eks: x^3): ")

# Få basisen, eksponenten, og tallet i basen
base, eksponent, num_in_base = base_eksponent(funksjonsutrykk)
eksponent = int(eksponent)

if num_in_base:
    svar = f"{eksponent * int(num_in_base)}*{base.replace(num_in_base, '', 1)}**{eksponent - 1}"
else:
    svar = f"{eksponent}*{base}**{eksponent - 1}"
    
    ''' 
    Alt dette er for debugging og mer output
    
    print("Ingen tall i basen")

# Skriv ut basisen, eksponenten, og tallet i basen
print("Base:", base)
print("Eksponent:", eksponent)

if num_in_base:
    print("Tall i basen:", num_in_base)
    '''

print(svar)
