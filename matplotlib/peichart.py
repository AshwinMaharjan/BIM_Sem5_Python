import matplotlib.pyplot as plt
#data
sizes=[80,90,95,100]
labels=['Ashwin','Nupur','Rojan','Soyal']
colors=['yellow','red','blue','pink']
explode=(0.1,0,0,0) #extract aalikati the 1st slice

#pie chart
plt.pie(sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct='%.2f%%',
        shadow=True, 
        startangle=140)

plt.title("Simple Bar Chart")

plt.show()