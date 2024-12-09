import math

R = 3
points = []

for x in range(-R, R + 1):
    for y in range(-R, R + 1):
        for z in range(-R, R + 1):
            if x**2 + y**2 + z**2 == R**2:
                points.append((x, y, z))

print(f"Antall punkter med heltallige koordinater på K: {len(points)}")
print("Punkter:", points)
