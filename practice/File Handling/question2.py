#Write a Python program that reads a file character by character and stops when it encounters the first vowel.

vowels='aeiouAEIOU'
with open('question2.txt','r') as file:
    while True:
        char=file.read(1) #character by character read
        if not char:
            print("No vowels found")
            break
        if char in vowels:
            print(f"Vowels found: {char}")
            break
