# Function to count alphabets, digits, and special characters
def count_characters(input_string):
    alphabets = 0
    digits = 0
    special_characters = 0

    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special_characters += 1

    return alphabets, digits, special_characters

# Read a string from the user
user_input = input("Enter a string: ")

# Get the counts
alphabets, digits, special_characters = count_characters(user_input)

# Display the results
print("\nCharacter counts:")
print(f"Number of alphabets: {alphabets}")
print(f"Number of digits: {digits}")
print(f"Number of special characters: {special_characters}")
