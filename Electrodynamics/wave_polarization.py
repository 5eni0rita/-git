import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate the wave at a given time
def calculate_wave(t, amplitude, frequency, initial_phase):
    return amplitude * np.sin(2 * np.pi * frequency * t + initial_phase)

# Set parameters for the waves
A1 = 1.0
f1 = 1.0
phi1 = 0.0

A2 = 0.5
f2 = 2.0
phi2 = np.pi/2

# Generate time values
t = np.linspace(0, 2, 1000)

# Calculate the individual waves
wave1_amplitude = calculate_wave(t, A1, f1, phi1)
wave2_amplitude = calculate_wave(t, A2, f2, phi2)

# Plot the individual waves in 2D
plt.figure(figsize=(12, 4))

# i) 2-D plot for the first wave
plt.subplot(121)
plt.plot(t, wave1_amplitude, label=f'Wave 1: $\phi_1={phi1}$')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Wave 1')
plt.legend()

# ii) 2-D plot for the second wave
plt.subplot(122)
plt.plot(t, wave2_amplitude, label=f'Wave 2: $\phi_2={phi2}$')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Wave 2')
plt.legend()

plt.tight_layout()
plt.show()

# Create a 3D plot for the propagation of the waves
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the first wave
ax.plot(t, wave1_amplitude, np.zeros_like(t), label='Wave 1')
# Plot the second wave
ax.plot(t, np.zeros_like(t), wave2_amplitude, label='Wave 2')

ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_zlabel('Amplitude')
ax.set_title('Propagation of Two Waves')

plt.legend()
plt.show()

# Calculate the resultant superposed wave
resultant_wave = wave1_amplitude + wave2_amplitude

# Plot the resultant superposed wave traveling along the z-axis
plt.plot(t, resultant_wave)
plt.xlabel('Time')
plt.ylabel('Resultant Amplitude')
plt.title('Resultant Superposed Wave')
plt.show()

# Additional scenarios:

# i) Linear wavefront at 45 degrees
angle = np.radians(45)
resultant_wave_linear_45 = np.cos(angle) * wave1_amplitude + np.sin(angle) * wave2_amplitude

# Plot the resultant wave with a linear wavefront at 45 degrees
plt.plot(t, resultant_wave_linear_45)
plt.xlabel('Time')
plt.ylabel('Resultant Amplitude')
plt.title('Resultant Wave - Linear Wavefront at 45 degrees')
plt.show()

# ii) Circular wavefront
resultant_wave_circular = np.sqrt(wave1_amplitude**2 + wave2_amplitude**2)

# Plot the resultant wave with a circular wavefront
plt.plot(t, resultant_wave_circular)
plt.xlabel('Time')
plt.ylabel('Resultant Amplitude')
plt.title('Resultant Wave - Circular Wavefront')
plt.show()

# iii) Elliptical wavefront due to phase difference
phase_difference = phi2 - phi1
resultant_wave_elliptical_phase = A1 * np.sin(2 * np.pi * f1 * t + phi1 + phase_difference/2) + A2 * np.sin(2 * np.pi * f2 * t + phi2 - phase_difference/2)

# Plot the resultant wave with an elliptical wavefront (phase difference)
plt.plot(t, resultant_wave_elliptical_phase)
plt.xlabel('Time')
plt.ylabel('Resultant Amplitude')
plt.title('Resultant Wave - Elliptical Wavefront (Phase Difference)')
plt.show()

# iv) Elliptical wavefront due to amplitude difference
resultant_wave_elliptical_amplitude = A1 * np.sin(2 * np.pi * f1 * t + phi1) + A2 * np.sin(2 * np.pi * f2 * t + phi2) / 2

# Plot the resultant wave with an elliptical wavefront (amplitude difference)
plt.plot(t, resultant_wave_elliptical_amplitude)
plt.xlabel('Time')
plt.ylabel('Resultant Amplitude')
plt.title('Resultant Wave - Elliptical Wavefront (Amplitude Difference)')
plt.show()

# v) Linear wavefront at an arbitrary angle
arbitrary_angle = np.radians(30)  # You can adjust this angle as needed
resultant_wave_linear_arbitrary = np.cos(arbitrary_angle) * wave1_amplitude + np.sin(arbitrary_angle) * wave2_amplitude

# Plot the resultant wave with a linear wavefront at an arbitrary angle
plt.plot(t, resultant_wave_linear_arbitrary)
plt.xlabel('Time')
plt.ylabel('Resultant Amplitude')
plt.title('Resultant Wave - Linear Wavefront at Arbitrary Angle')
plt.show()