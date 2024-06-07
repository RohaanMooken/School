def løs(tall, rest):
    x = 15
    while True:
        for i in range(len(tall)):
            if x % tall[i] != rest[i]:
                break
        else:
            return x
        x += 15
        
tall = [17, 16, 15]
rest = [3, 10, 0]
print(løs(tall, rest))
x = løs(tall, rest)
print("aasdasdad", x%15, x%16, x%17)


print(x)