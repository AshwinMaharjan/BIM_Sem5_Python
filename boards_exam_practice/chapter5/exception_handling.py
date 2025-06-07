try:
    num=int(input("Enter a number: "))
    result=10/num
except ZeroDivisionError as e:
    print("Error: ",e)
except ValueError as v:
    print("Error: ",v)
else:
    print("Result: ",result)
finally:
    print("This code executes anyhow")