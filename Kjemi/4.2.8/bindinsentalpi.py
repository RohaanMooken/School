from pylab import *

data = loadtxt('bindingsentalpi.txt', dtype = str, skiprows = 1)

atom1 = data[:,0]
atom2 = data[:,1]
bindingsorden = data[:,2]
reaksjonsentalpi = data[:,3]


a1 = input("Første atom: ")
a2 = input("Andre atom: ")
orden = input("Bindingsorden: ")

for i in range(len(atom1)):
        if atom1[i] == a1 and atom2[i] == a2 and bindingsorden[i] == orden:
            indeks = i
            print("Reaksjonsentalpien er:", reaksjonsentalpi[i], "kJ.")