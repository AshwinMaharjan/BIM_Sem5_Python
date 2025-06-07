import numpy as np
import matplotlib.pyplot as plt

#data
data=np.random.randn(1000)

plt.hist(data,bins=30,edgecolor="black")

plt.title("Histogram")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()