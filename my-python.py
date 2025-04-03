import numpy as np
import matplotlib.pyplot as plt

# Input parameters
M_design = 3.5  # Design Mach number
num_waves = 3  # Number of expansion waves
gamma = 1.4  # Ratio of specific heat
T_combustion = 3000  # Combustion chamber temperature (K)
P_combustion = 100000  # Combustion chamber pressure (Pa)
A_throat = 0.01  # Throat area (m^2)
P_ambient = 101325  # Ambient pressure (Pa)

# Function to calculate pressure ratio at the throat
def PR_throat_over_P_ambient(M_design, P_throat_over_P_ambient):
    return P_throat_over_P_ambient

# Function to calculate exit Mach number for bell nozzle
def bell_nozzle_exit_Mach(M_design, P_throat_over_P_ambient, gamma, P_ambient):
    return np.sqrt(P_throat_over_P_ambient * (2 / (gamma - 1)) * (1 - (P_ambient / P_throat_over_P_ambient)**((gamma - 1) / gamma)))

# Calculate exit pressure
# Use the Prandtl-Meyer function to find the exit Mach number
M_exit = bell_nozzle_exit_Mach(M_design, P_throat_over_P_ambient(M_design, P_combustion / P_ambient), gamma, P_ambient)
P_exit = P_ambient * np.exp(gamma * (1 - 1 / M_exit**2)**0.5)

# Calculate exit area
A_exit = A_throat * (M_exit / M_design)**2

# Calculate number of wall divisions
num_divisions = 100  # Adjust as needed

# Create a curvilinear mesh
x, y = np.meshgrid(np.linspace(0, 1, num_waves + 2), np.linspace(0, 1, num_divisions + 1))

# Define the bell nozzle contour
r_throat = np.sqrt(A_throat / np.pi)
r_bell = lambda x: r_throat * (1.5 * (1 - x) + 0.382 * (1 - x)**2)

# Create a curvilinear mesh
x_mesh, y_mesh = np.meshgrid(np.linspace(0, 1, num_waves + 2), r_bell(np.linspace(0, 1, num_divisions + 1)))

# Calculate positions along the centerline
x_centerline = np.linspace(0, 1, num_divisions + 1)
r_centerline = r_bell(x_centerline)
z_centerline = np.sqrt(A_exit - np.pi * r_centerline**2)

# Calculate wall positions
r_wall = r_bell(np.linspace(0, 1, num_divisions + 1))
theta_wall = np.arctan(np.diff(r_wall) / np.diff(z_centerline))
x_wall = x_mesh * np.cos(theta_wall) - y_mesh * np.sin(theta_wall)

# Plot the results
plt.figure()
plt.plot(x_centerline, z_centerline, 'b-', x_wall, z_centerline, 'r-')
plt.xlabel('x')
plt.ylabel('z')
plt.title('Bell Nozzle Contour and Centerline')
plt.show()
