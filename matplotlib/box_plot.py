import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.normal(0, 1, 100)  # Normally distributed data

# Create a box plot
plt.boxplot(data)

# Title and labels
plt.title("Basic Box Plot")
plt.xlabel("Data")
plt.ylabel("Values")

# Show plot
plt.show()
