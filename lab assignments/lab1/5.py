import re

# Read a multi-sentence string from the user
user_input = input("Enter a multi-sentence string: ")

# Separate each sentence
sentences = re.split(r'[.!?]', user_input)
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  # Remove empty and trailing spaces

# Display each sentence
print("\nSentences:")
for i, sentence in enumerate(sentences, start=1):
    print(f"Sentence {i}: {sentence}")

# Separate each word (excluding commas)
words = re.findall(r'\b\w+\b', user_input)

# Display each word
print("\nWords:")
for i, word in enumerate(words, start=1):
    print(f"Word {i}: {word}")
