import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Funksjon for å beregne kryssprodukt-sekvensen
def calculate_sequence(a0, v, n):
    sequence = [a0]
    for i in range(1, n):
        next_vector = np.cross(sequence[-1], v)
        sequence.append(next_vector)
    return sequence

# Funksjon for å plotte en sekvens
def plot_sequence(sequence, title, ax):
    for vec in sequence:
        ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color='b', length=0.5)
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

# Definer ulike kombinasjoner av a0 og v
examples = [
    (np.array([1, 0, 0]), np.array([0, 1, 0]), "Example 1"),
    (np.array([0, 1, 0]), np.array([0, 0, 1]), "Example 2"),
    (np.array([1/3, 1/3, 1/3]), np.array([1/2, -1/2, 0]), "Example 3"),
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0, 0, -1]), "Example 4"),
    (np.array([1/4, -1/4, 1/2]), np.array([-1/3, 1/3, -1/3]), "Example 5"),
    (np.array([-1/2, 1/3, -1/3]), np.array([1/4, -1/4, 1/2]), "Example 6"),
    (np.array([1/5, -1/5, 1/5]), np.array([-1/6, 1/6, -1/6]), "Example 7"),
    (np.array([-1/3, 1/3, -1/2]), np.array([1/5, -1/5, 1/5]), "Example 8"),
]
# Lag en figur med flere subplotter
fig = plt.figure(figsize=(15, 15))

# Beregn antall rader og kolonner for subplottene
n_rows = int(np.ceil(len(examples) / 2))
n_cols = 2

for i, (a0, v, title) in enumerate(examples):
    n_vectors = len(a0)
    sequence = calculate_sequence(a0, v, n_vectors)
    ax = fig.add_subplot(n_rows, n_cols, i + 1, projection='3d')
    plot_sequence(sequence, title, ax)

plt.tight_layout()
plt.show()