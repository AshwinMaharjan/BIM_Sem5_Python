import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [3, 4, 6, 7, 8]
y2 = [5, 6, 7, 8, 10]

# Create 1 row and 2 columns of subplots
plt.subplot(1, 2, 1)  # 1 row, 2 columns, plot 1
plt.plot(x, y1, label="Line")
plt.title("Line Plot")

plt.subplot(1, 2, 2)  # 1 row, 2 columns, plot 2
plt.scatter(y1, y2, color='red')
plt.title("Scatter Plot")

plt.tight_layout()  # Adjust spacing
plt.show()
