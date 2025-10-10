import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
y = np.sin(x)
z = np.cos(x)

# To get matplotlib to display the plots, we use plt.show()
# To create a new figure, we use plt.figure()

plt.figure(figsize=(10, 6))  # Set the figure size (optional)
plt.plot(x, y, "o")  # Plot
plt.show()

plt.figure(figsize=(10, 6))  # Set the figure size (optional)
plt.plot(x, z)  # Plot
plt.show()

# labeling a plot

plt.figure(figsize=(10, 6))  # Set the figure size (optional)
plt.plot(x, y)
plt.plot(x, z)
plt.title("Sine and Cosine Wave")  # Title of the plot
plt.xlabel("X (radians)")  # Label for the x-axis
plt.ylabel("Y data")  # Label for the y-axis
plt.legend(["sin(x)", "cos(x)"])  # Legend to differentiate the lines
plt.show()