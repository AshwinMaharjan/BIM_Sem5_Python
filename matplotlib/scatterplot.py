import matplotlib.pyplot as plt

#data
x=[1,2,3,4,5]
y=[2,3,5,7,11]

#scatter_plot
plt.scatter(x,y)

#add a title and label name
plt.title("Simple Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

#show the plot
plt.show()