import matplotlib.pyplot as plt

#DATA
categoies=['A','B','C','D','E']
values=[4,7,1,8,10]

plt.bar(categoies,values)

plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()