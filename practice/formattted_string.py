name="ashwin"
age=20

# formatted_string="Name:"+name+" Age:"+str(age)
# print(formatted_string)

# formatted_string="Name:{}, Age:{}".format(name,age)
# print(formatted_string)

formatted_string=f"Name:{name}, Age:{age}"
print(formatted_string)

formatted_string="Name:%s, Age:%d"%(name,age)
print(formatted_string)
