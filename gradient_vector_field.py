import matplotlib.pyplot as plt
import numpy as np

# 1. Define range from -10 to 10 with 0.01 step length
x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)

mesh_x, mesh_y = np.meshgrid(x, y)

# 2. Calculate z function's value
z_for_variant_4 = np.arctan(mesh_x * mesh_y)
z_for_variant_10 = np.arctan(mesh_x / mesh_y)

# 3. Draw pictures for 4 and 10 variants
figure = plt.figure()

ax = figure.add_subplot(111, projection="3d")
ax.plot_surface(mesh_x, mesh_y, z_for_variant_4, rstride=5, cstride=10)

plt.show()

figure = plt.figure()

ax = figure.add_subplot(111, projection="3d")
ax.plot_surface(mesh_x, mesh_y, z_for_variant_10, rstride=5, cstride=10)

plt.show()
