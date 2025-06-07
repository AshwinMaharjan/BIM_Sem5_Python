with open('demo_file.txt','r') as file:
    words=file.read().split()

    for word in words:
        print(word)