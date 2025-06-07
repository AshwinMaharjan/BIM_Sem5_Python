import matplotlib.pyplot as plt
import numpy as np

#data
data=np.random.randn(1000)

#histogram
plt.hist(data,bins=30,edgecolor="black")

plt.title("Histogram")
plt.xlabel('Value')
plt.ylabel('Frequencies')

plt.show()


