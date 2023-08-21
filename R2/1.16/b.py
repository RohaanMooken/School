a = [1, 1]

for i in range(18):
    a.append(a[i]+a[i + 1])
    print(a[i + 1]/a[i])