import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.sin(x)

# Line Plot
plt.plot(x, y)
plt.title("Line Graph")
plt.show()

# Bar Chart
plt.bar(["A", "B", "C"], [10, 20, 15])
plt.title("Bar Chart")
plt.show()

# Pie Chart
plt.pie([40, 30, 30], labels=["A", "B", "C"], autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

