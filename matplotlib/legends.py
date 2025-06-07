import matplotlib.pyplot as plt

#data
x=[1,2,3,4,5]
y1=[2,3,5,7,11]
y2=[1,4,6,8,10]

#line plots
plt.plot(x,y1,label='Line 1')
plt.plot(x,y2,label='Line 2')

#add legend
plt.legend()

plt.title("Line Plot with Legend")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()

