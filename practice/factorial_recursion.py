def factorial(num):
    if num==0 or num==1:
        return 1 #base case
    else:
        return num*factorial(num-1)
    
a=int(input("Enter the number: "))
fact=factorial(a)
print("The factorial of",a,"is",fact)