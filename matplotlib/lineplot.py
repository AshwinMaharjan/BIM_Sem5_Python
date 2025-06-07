import matplotlib.pyplot as plt

#data
x=[1,2,3,4,5]
y=[2,3,5,7,11]

#create a line plot
plt.plot(x,y)

#add a title and labels
plt.title("Simple Line Plot")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

#show the plot
plt.show()
