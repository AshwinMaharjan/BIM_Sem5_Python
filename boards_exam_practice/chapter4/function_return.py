def square(x):
    return x * x
# num=5
num=int(input("Enter the number: "))
result=square(num)
print("The square value of ",num,"is: ",result)

#multiple_values
def student_info():
    name="Ashwin"
    age=20
    address="Nayabazar"
    college="Prime College"
    return name,age,address,college
info=student_info()
print(info)

#another example
def calculate(num1,num2):
    sum=num1+num2
    diff=num1-num2
    mul=num1*num2
    return sum,diff,mul
sum_value,diff_value,mul_value=calculate(10,5)
print("Sum value: ",sum_value)
print("Difference value: ",diff_value)
print("Multiplication value: ",mul_value)
