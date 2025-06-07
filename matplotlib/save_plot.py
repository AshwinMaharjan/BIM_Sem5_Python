import matplotlib.pyplot as plt

#data
x=[1,2,3,4,5]
y=[10,20,30,40,50]

#line plot
plt.plot(x,y)
plt.title("Saving Plot")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.savefig('line_plot.png')
plt.show()
