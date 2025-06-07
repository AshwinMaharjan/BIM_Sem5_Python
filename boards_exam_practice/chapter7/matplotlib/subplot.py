import matplotlib.pyplot as plt

#data
x=[1,2,3,4,5]
y1=[2,3,4,6,7]
y2=[3,4,5,6,9]

#1st plot
plt.subplot(1,2,1)
plt.plot(x,y1,label="Label 1",color="Red")
plt.title("1st Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

#2nd plot
plt.subplot(1,2,2)
plt.scatter(x,y2,label="Label 2")
plt.title("2nd Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.tight_layout()
plt.show()


