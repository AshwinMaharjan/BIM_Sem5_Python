def square(x):
    return x*x
print(square(5))

def student_info():
    name="Ashwin"
    age=20
    address="Kathmandu"
    return name,age,address
info=student_info()
print(info)


def calculate(a,b):
    sum=a+b
    diff=a-b
    mul=a*b
    return sum,diff,mul
sum_value,diff_value,mul_value=calculate(10,5)
print(sum_value)
print(diff_value)
print(mul_value)
