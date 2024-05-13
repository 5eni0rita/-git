import numpy as np
from scipy.linalg import eigh

# Define atomic number and basis set
Z = 4  # Atomic number of beryllium
N = 2  # Number of electrons
n_basis = 2  # Number of atomic orbitals (1s, 2s, 2p)

# Define atomic orbital energies (1s, 2s, 2p)
epsilon = np.array([-11.10, -0.50])

# Construct the core Hamiltonian
H_core = np.diag(epsilon)

# Calculate the two-electron repulsion integrals (assuming closed-shell configuration)
# These are constants and can be precomputed for efficiency
eri = np.zeros((n_basis, n_basis, n_basis, n_basis))  # Initialize ERIs to zero
# Assuming closed-shell configuration, only need two-electron repulsion integrals for 2 electrons
eri[0, 0, 0, 0] = 1.25  # (1s, 1s, 1s, 1s)
eri[1, 1, 1, 1] = 0.80  # (2s, 2s, 2s, 2s)
# Coulomb and exchange integrals for off-diagonal elements are zero in this simplified example

# Hartree-Fock iterations
max_iter = 1000
tolerance = 1e-8

# Function to construct the Fock matrix
def construct_fock_matrix(D):
    J = np.einsum('pqrs,rs->pq', eri, D)
    K = np.einsum('prqs,rs->pq', eri, D)
    F = H_core + 2 * J - K
    return F

# Initialize density matrix
D = np.zeros((n_basis, n_basis))

# Perform Hartree-Fock iterations
for iteration in range(max_iter):
    F = construct_fock_matrix(D)
    energy, C = eigh(F)
    C_occ = C[:, :N]
    D_new = np.dot(C_occ, C_occ.T)
    if np.allclose(D, D_new, atol=tolerance):
        break
    D = D_new

# Compute the first ionization energy
ionization_energy_1 = energy[0] - 2 * epsilon[0]
print("First ionization energy of Be:", ionization_energy_1)

# Compute the second ionization energy
ionization_energy_2 = energy[1] - 2 * epsilon[0]
print("Second ionization energy of Be:", ionization_energy_2)