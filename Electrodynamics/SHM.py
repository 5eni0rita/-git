import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega = 1.0  # Oscillator frequency

# Define the ladder operators
def ladder_plus(n):
    return np.sqrt(n + 1)

def ladder_minus(n):
    return np.sqrt(n)

# Define the potential energy function
def V(x):
    return 0.5 * omega**2 * x**2

# Define the Hamiltonian operator
def Hamiltonian(n):
    return omega * (n + 0.5)

# Define the wave function
def psi_n(x, n):
    return (1 / np.sqrt(2**n * np.math.factorial(n))) * (omega / np.pi)**0.25 * np.exp(-0.5 * omega * x**2) * np.polynomial.hermite.hermval(np.sqrt(omega) * x, [0] * n + [1])

# Define normalization constant
def normalization_constant(n):
    return 1 / np.sqrt(2**n * np.math.factorial(n))

# Define probability density
def prob_density(x, n):
    return np.abs(psi_n(x, n))**2

# Define the range for x
x_values = np.linspace(-5, 5, 1000)

# Calculate and plot the first five eigenstates and their probability densities
plt.figure(figsize=(12, 8))
for n in range(5):
    plt.subplot(5, 2, 2*n+1)
    plt.plot(x_values, psi_n(x_values, n), label=f"n={n}")
    plt.title(f"Eigenfunction for n={n}")
    plt.xlabel('x')
    plt.ylabel('$\psi_n(x)$')
    plt.legend()

    plt.subplot(5, 2, 2*n+2)
    plt.plot(x_values, prob_density(x_values, n), label=f"n={n}")
    plt.title(f"Probability Density for n={n}")
    plt.xlabel('x')
    plt.ylabel('$|\psi_n(x)|^2$')
    plt.legend()

plt.tight_layout()
plt.show()
