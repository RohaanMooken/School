figur = int(input("N = "))
figur_sum = 0 
sum = 0
n = figur

def calculate_figur(n):
    figur_sum = 0
    while n > 0:
        current = n ** 2
        figur_sum = figur_sum + current
        n -= 1
    return figur_sum

while figur > 0:
    figur_sum = calculate_figur(figur)
    sum = sum + figur_sum
    figur -=1
    
print("Summern av figuren:", sum)