import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
k_B = 1.38e-23  # Boltzmann constant in J/K
h = 6.63e-34  # Planck constant in Js

def fermi_dirac(E, E_F, T):
    """
    Fermi-Dirac distribution function.
    E: Energy
    E_F: Fermi energy
    T: Temperature
    """
    return 1 / (np.exp((E - E_F) / (k_B * T)) + 1)

def mean_occupation(E_F, T):
    """
    Mean occupation number.
    E_F: Fermi energy
    T: Temperature
    """
    E = np.linspace(0, 10 * E_F, 1000)
    n_E = fermi_dirac(E, E_F, T)
    return quad(lambda E: n_E, 0, np.inf)[0]

def heat_capacity(E_F, T):
    """
    Heat capacity at constant volume for Fermi gas.
    E_F: Fermi energy
    T: Temperature
    """
    E = np.linspace(0, 10 * E_F, 1000)
    n_E = fermi_dirac(E, E_F, T)
    return quad(lambda E: E * n_E, 0, np.inf)[0] / T

def entropy(E_F, T):
    """
    Entropy for Fermi gas.
    E_F: Fermi energy
    T: Temperature
    """
    E = np.linspace(0, 10 * E_F, 1000)
    n_E = fermi_dirac(E, E_F, T)
    return k_B * quad(lambda E: -n_E * np.log(n_E) - (1 - n_E) * np.log(1 - n_E), 0, np.inf)[0]

# Fermi energy
E_F = 1e-19  # Just an example value, you should adjust this

# Temperature range
T_range = np.linspace(1, 1000, 100)

# Calculate quantities
mean_occ = [mean_occupation(E_F, T) for T in T_range]
heat_cap = [heat_capacity(E_F, T) for T in T_range]
entropies = [entropy(E_F, T) for T in T_range]

# Plotting
plt.figure(figsize=(12, 8))

# Mean Occupation Number
plt.subplot(3, 1, 1)
plt.plot(T_range, mean_occ, label='Mean Occupation Number')
plt.xlabel('Temperature (K)')
plt.ylabel('Mean Occupation')
plt.title('Mean Occupation Number vs Temperature')
plt.legend()

# Heat Capacity
plt.subplot(3, 1, 2)
plt.plot(T_range, heat_cap, label='Heat Capacity')
plt.xlabel('Temperature (K)')
plt.ylabel('Heat Capacity (J/K)')
plt.title('Heat Capacity vs Temperature')
plt.legend()

# Entropy
plt.subplot(3, 1, 3)
plt.plot(T_range, entropies, label='Entropy')
plt.xlabel('Temperature (K)')
plt.ylabel('Entropy (J/K)')
plt.title('Entropy vs Temperature')
plt.legend()

plt.tight_layout()
plt.show()
