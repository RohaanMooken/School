sum = 0
x = 1
n = 8
a = 1
b = 5
deltax = (b-a)/n
for i in range(n):
    sum += x**2
    x += deltax
print(sum/n)