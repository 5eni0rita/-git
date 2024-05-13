import matplotlib.pyplot as plt
import numpy as np

# Given data
temperature = [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30]
resistance = [0.5735, 0.5637, 0.5588, 0.5539, 0.5441, 0.5392, 0.5294, 0.5294, 0.5147, 0.5049, 0.4951, 0.4902]

# Plotting
plt.plot(temperature, resistance, marker='o', linestyle='-', label='Data', color='black')
plt.title('Resistance vs Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Resistance (Ω)')
plt.grid(True)

# Calculate the slope and intercept for the trend line
slope, intercept = np.polyfit(temperature, resistance, 1)

# Calculate the trend line values
trend_line = [slope * temp + intercept for temp in temperature]

# Plot the trend line
plt.plot(temperature, trend_line, color='green', linestyle='--', label='Trend Line')

# Show legend
plt.legend()

# Show plot
plt.show()

print("Slope:", slope)
