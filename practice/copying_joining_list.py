student=['ashwin','nupur','soyal','rojan']

print("Using copy()")
new_student1=student.copy()
print(new_student1)

print("Using slice[:]")
new_student2=student[:]
print(new_student1)

print("Using list()")
new_student3=list(student)
print(new_student1)

country1=['Nepal','India','China']
country2=['Portugal','France','Spain']

print("Using + operator")
combined=country1+country2
print(combined)

print("Using extend()")
country1.extend(country2)
print(country1)