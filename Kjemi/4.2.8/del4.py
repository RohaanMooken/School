atom1 = []
atom2 = []
bindingsorden = []
reaksjonsentalpi = []

with open('bindingsentalpi.txt', 'r') as file:
    next(file)
    for line in file:
        parts = line.split()
        atom1.append(parts[0].strip())
        atom2.append(parts[1].strip())
        bindingsorden.append(parts[2].strip())
        reaksjonsentalpi.append(parts[3].strip())

a1 = input("Første atom: ").strip()
a2 = input("Andre atom: ").strip()
orden = input("Bindingstype: ").strip()

for i in range(len(atom1)):
    current_atom1 = atom1[i]
    current_atom2 = atom2[i]
    current_bindingsorden = bindingsorden[i]

    if current_atom1 == a1 and current_atom2 == a2 or current_atom1 == a2 and current_atom2 == a1 and current_bindingsorden == orden:
        print("Reaksjonsentalpien er:", reaksjonsentalpi[i], "kJ.")
