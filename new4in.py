from pygasflow import CD_Min_Length_Nozzle
import csv
import matplotlib.pyplot as plt
import numpy as np

# Nozzle parameters
Ri = 0.050   # Inlet Radius
Rt = 0.014  # Throat Radius
Re = 0.0365 # Exit (outlet) Radius
Rj = 0.0105  #0.75*Rt
R0 = 0.021 #1.5 Rt
theta_c = 45 # half cone angle of the convergent
theta_N = 15   # half cone angle of the divergent

# Create nozzle object
nozzle = CD_Min_Length_Nozzle(Ri, Re, Rt, Rj, R0, theta_c, 10)

# Build geometry with more points for accuracy
x_full, y_full = nozzle.build_geometry(1000)

# Sample 100 points evenly along the curve
indices = np.linspace(0, len(x_full)-1, 100, dtype=int)
x_100 = [x_full[i] for i in indices]
y_100 = [y_full[i] for i in indices]

# Plot full curve and sampled points
plt.figure()
plt.plot(x_full, y_full, label='Full Curve', color='blue')
plt.scatter(x_100, y_100, label='100 Points', color='red')
plt.xlabel("Length")
plt.ylabel("Radius")
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()

# Save coordinates to CSV
with open('nozzle_geometry_100points.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Length', 'Radius'])
    for i in range(len(x_100)):
        writer.writerow([x_100[i], y_100[i]])

print("100 coordinates saved to 'nozzle_geometry_100points.csv'")
