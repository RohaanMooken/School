import matplotlib.pyplot as plt


data = [
    [0, 13177, 409326, 2636, 2366],
    [21, 8724, 458798, 1199, 601],
    [5085, 24871, 142183, 2106, 17],
    [2680, 16632, 18986, 2065, 0],
    [653, 12091, 7660, 1335, 0],
    [456, 5965, 13905, 802, 0],
    [414, 6507, 8093, 539, 0],
    [1654, 23696, 4201, 1576, 0],
    [3219, 27969, 2236, 2021, 0],
    [7001, 18298, 2597, 2900, 0],
    [15491, 63323, 4171, 6954, 0],
    [13544, 126291, 5989, 7127, 0]
]


x_list = []
y_list = []
x = 0


for i in range(len(data[0])):
    for j in range(len(data)):
        y = data[j][i]
        # print(y)
        y_list.append(y)
        x_list.append(x)
        x+=1
        
plt.plot(x_list, y_list)
plt.grid()
plt.show()
newdata = []
count = 0
x_temp_list = []
for i in range(len(y_list)):
    newdata.append(y_list[i])
    x_temp_list.append(count)
    count+=1
    

for _ in range(12*2):
    newdata.pop(-1)
    x_temp_list.pop(-1)


print(newdata)

plt.plot(x_temp_list, newdata)
plt.show()
