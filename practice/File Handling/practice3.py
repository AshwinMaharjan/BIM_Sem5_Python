with open("practice1.txt","r") as file:
    data=file.read()
    print(data)

    if(data.find("learning")!=-1):
        print("FOUND")
    else:
        print("NOT FOUND")
