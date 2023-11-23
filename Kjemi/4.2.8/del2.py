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