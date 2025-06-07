#WAP to read multiple lines from user until user type 'asian' then stores all strings into asian.txt file

lines = []
print("Enter the text(type asian when you want to stop): ")

while True:
    user_input=input()
    if user_input.lower() == 'asian':
        break
    lines.append(user_input)

with open('asian.txt','w') as file:
    for line in lines:
        file.write(line + '\n')

print("SUCCESS")
    