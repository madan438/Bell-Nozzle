from pygasflow.nozzles.moc import min_length_supersonic_nozzle_moc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ht = 0.0037
n = 20
Me = 4.2
gamma = 1.133

# Generate nozzle wall coordinates
wall, _, _, _ = min_length_supersonic_nozzle_moc(ht, n, Me, None, gamma)

# Plotting
plt.figure()

# Plot nozzle wall
plt.plot(wall[:, 0], wall[:, 1], "k")

# Add labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$M_e$ = {}, n = {}, ht = {} ".format(Me, n, ht))

# Add grid and equal axis
plt.grid()
plt.axis('equal')
plt.tight_layout()

# Display plot
plt.show()

# Create DataFrame
data = pd.DataFrame({'x': wall[:, 0], 'y': wall[:, 1]})

# Save to CSV
data.to_csv('nozzle_wall_coordinates.csv', index=False)
