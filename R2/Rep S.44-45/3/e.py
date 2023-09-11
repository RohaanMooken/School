radioer = 580
sum = 0

for i in range(1000):
    print(f"{i + 1}\t{radioer}")
    if sum >= 10000:
        break
    sum += radioer
    radioer += 30

print(f"De har produsert 10000 radioer etter {i - 1} måneder")