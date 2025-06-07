fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#another example
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#another example
newlist = [x for x in fruits]
print(newlist)

#another example
newlist = [x for x in range(10,15)]
print(newlist)

#same eg but with condition
newlist=[x for x in range(10,15) if x>12]
print(newlist)

#same eg but with condition
newlist=[x for x in range(10,15) if x<12]
print(newlist)

#uppercase
newlist = [x.upper() for x in fruits]
print(newlist)

newlist=['Helloo' for x in fruits]
print(newlist)

