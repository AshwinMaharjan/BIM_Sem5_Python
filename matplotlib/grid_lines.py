import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 8]

# Plotting the data
plt.plot(x, y, label="Line")

# Add grid lines
plt.grid(True)  # Default grid lines (both x and y)

# Title and labels
plt.title("Simple Grid Lines Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show plot
plt.legend()
plt.show()
