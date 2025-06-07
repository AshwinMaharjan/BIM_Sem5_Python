marks=int(input("Enter the marks of the student:"))

if(marks >= 90):
    print("The marks is A+")
elif(marks<90 and marks>=80):
    print("The marks is A")
elif(marks<80 and marks>=70):
    print("The marks is B+")
elif(marks<70 and marks>=60):
    print("The marks is B")
else:
    print("The marks below B")
    