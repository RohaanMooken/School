print("Tast 1 for ikke-metall og 2 for metall")

stoff1 = int(input("Stoff 1: "))
stoff2 = int(input("Stoff 2: "))
if stoff1 == 1 and stoff2 == 1:
    print("Dette blir en kovalent.")
elif stoff1 == 1 and stoff2 == 2 or stoff1 == 2 and stoff2 == 1:
    print("Dette blir en inonebinding.")
else:
    print("Dette blir en metallbinding.")