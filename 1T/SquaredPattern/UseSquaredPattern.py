# NOT DONE!!
# DO NOT USE

klosser = int(input("N = "))
figur_sum = 0 
sum = 0
n = klosser


def calculate_figur(n):
    figur_sum = 0
    while n > 0:
        current = n ** 2
        figur_sum = figur_sum + current
        n -= 1
    return figur_sum

while klosser > 0:
    figur_sum = calculate_figur(klosser)
    sum = sum + figur_sum
    klosser -=1
    
print("Summern av figuren:", sum)