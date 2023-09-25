def pentagon(n):
    if n == 1:
        return 1
    return pentagon(n - 1) + (3 * n - 2)

# while True:
#     n = int(input("Tall: "))
#     print(pentagon(n))

for i in range(1, 11):
    print(f"{i}\t{pentagon(i)}")