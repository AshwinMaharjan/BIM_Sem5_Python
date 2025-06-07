
# Removing blank lines and converting text to uppercase
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        if line.strip():
            outfile.write(line.upper())

print("Processed text written to 'output.txt'.")
