num=int(input("Enter the number: "))

if num==0 or num==1:
    print("The entered number is a composite number")
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            print("The entered number is a composite number")
            break
    else:
        print("The entered number is a prime number")
else:
    print("The entered number is a composite number")



