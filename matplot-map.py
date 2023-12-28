import matplotlib.pyplot as plt
import numpy as np

# Read vector data
with open("Vector_201001022200.d", "r") as file:
    vector_data = file.read()

# Split the vector data into lines and extract coordinates
vector_lines = vector_data.strip().split('\n')
vector_coordinates = [list(map(float, line.split())) for line in vector_lines]

# Read tideland data
with open("tideland_201001022200.d", "r") as file:
    tideland_data = file.read()

# Split the tideland data into lines and extract coordinates
tideland_lines = tideland_data.strip().split('\n')
tideland_coordinates = [list(map(float, line.split())) for line in tideland_lines]

# Extract the range for x and y values from tideland_coordinates
x_min, x_max = np.min(tideland_coordinates, axis=0)[0], np.max(tideland_coordinates, axis=0)[0]
y_min, y_max = np.min(tideland_coordinates, axis=0)[1], np.max(tideland_coordinates, axis=0)[1]

# Include vector coordinates in the range calculation
x_min = min(x_min, np.min(vector_coordinates, axis=0)[0])
x_max = max(x_max, np.max(vector_coordinates, axis=0)[2])
y_min = min(y_min, np.min(vector_coordinates, axis=0)[1])
y_max = max(y_max, np.max(vector_coordinates, axis=0)[3])

# Vector plot
fig, ax = plt.subplots()
for x1, y1, x2, y2 in vector_coordinates:
    dx = x2 - x1
    dy = y2 - y1
    ax.arrow(x1, y1, dx, dy, head_width=20, head_length=30, fc='red', ec='red')

# Tideland plot
for x, y in tideland_coordinates:
    ax.plot(x, y, marker='o', linestyle='-', color='black')

# Contour plot for the matrix (41, 49)
# m, n = 41, 49
# x_values = np.linspace(x_min, x_max, n)
# y_values = np.linspace(y_min, y_max, m)

# # Create a meshgrid
# X, Y = np.meshgrid(x_values, y_values)

# # Create some sample data for the contour plot (replace this with your actual data)
# Z = np.random.rand(m, n)

# # Contour plot
# contour = ax.contour(X, Y, Z, cmap='viridis', alpha=0.5)

# # Add a colorbar for the contour plot
# cbar = fig.colorbar(contour, ax=ax, orientation='vertical')

# Set axis labels and show the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()
