import matplotlib.pyplot as plt
#data
x=[1,2,3,4,5]
y1=[4,5,6,7,8]
y2=[1,4,7,8,10]
plt.plot(x,y1,marker='s',label="Label1")
plt.plot(x,y2,marker='s',label="Label2")
plt.title("Color and Style")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

