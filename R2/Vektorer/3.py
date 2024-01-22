import math
import numpy as np

R = 3
points = []

for x in range(-3, 4):
    for y in range(-3, 4):
        for z in range(-3, 4):
            length = math.sqrt(x**2 + y**2 + z**2)
            if length == R:
                point = np.array([x, y, z])
                points.append(point)

print(points)
print(len(points))