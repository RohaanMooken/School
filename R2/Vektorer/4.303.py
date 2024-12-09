import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definer startvektoren a0 og vektoren v
a0 = np.array([(3/4)*np.sqrt(2), 0, 0])
v = np.array([1/3, 2/3, -2/3])

# Funksjon for å beregne kryssproduktet
def calculate_sequence(a0, v, n):
    sequence = [a0]
    for i in range(1, n):
        next_vector = np.cross(sequence[-1], v)
        sequence.append(next_vector)
    return sequence

# Beregn de seks første vektorene
n_vectors = 6
sequence = calculate_sequence(a0, v, n_vectors)

# Print de seks første vektorene
for i, vec in enumerate(sequence):
    print(f"Vector {i+1}: {vec}")

# Plotting av vektorene i et 3D-koordinatsystem
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Legg til hver vektor i plottet
for vec in sequence:
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color='b', length=0.05)

# Sett opp aksene
ax.set_xlim([-0.05, 0.05])
ax.set_ylim([-0.05, 0.05])
ax.set_zlim([-0.05, 0.05])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Første seks vektorer i følgen')

plt.show()