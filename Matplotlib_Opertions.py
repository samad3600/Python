# Matplotlib Opertions

import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave', color='blue')

# Add title and labels
plt.title('Sine Wave Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.grid()
plt.show()
