import numpy as np
import matplotlib.pyplot as plt

#data
sizes=[100,120,130,140,150]
labels=["Ashwin","Nupur","Rojan","Rojina","Yujal"]
colors=["Pink","Yellow","Blue","Green","Grey"]
explode=[0.1,0,0,0,0]

plt.pie(
    sizes,
    labels=labels,
    autopct="%.2f%%",
    colors=colors,
    explode=explode,
    shadow=True,
    startangle=140
)

plt.title("Pie Chart")
plt.show()