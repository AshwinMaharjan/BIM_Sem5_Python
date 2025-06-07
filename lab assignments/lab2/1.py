# Writing to file until user enters "bye"
with open("test.txt", "w") as file:
    while True:
        text = input("Enter text (type 'bye' to stop): ")
        if text.lower() == "bye":
            break
        file.write(text + "\n")

# Reading from file and displaying content
with open("test.txt", "r") as file:
    print("\nFile Contents:\n")
    print(file.read())
