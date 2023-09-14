# 1.4.29

Programmet nedenfor skal avgjøre om en binding blir ionisk, kovalent eller metallisk, men det fungerer ikke helt.

Skriv om programmet slik at det gjør det det skal.

```python
print("Tast 1 for ikke-metall og 2 for metall")

stoff1 = int(input("Stoff 1: "))
stoff2 = int(input("Stoff 2: "))
if stoff1 == 1 and stoff2 == 1:
    print("Dette blir en ionebinding.")
elif stoff1 == 1 and stoff2 == 2:
    print("Dette blir en kovalent binding.")
else:
    print("Dette blir en metallbinding.")
```