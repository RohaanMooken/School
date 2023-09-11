radioer = 580
sum = 0

for i in range(12):
    print(f"{i + 1}\t{radioer}")
    sum += radioer
    radioer += 30

print(f"2021: {sum}, solgte radioer")