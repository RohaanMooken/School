radioer = 580
sum = 0

for i in range(72):
    print(f"{i + 1}\t{radioer}")
    if i >= 60:
        sum += radioer
    radioer += 30

print(f"{2026}: {sum}, solgte radioer")