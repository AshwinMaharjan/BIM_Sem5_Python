# Merging two files into a single file
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as merged:
    merged.write(f1.read() + "\n" + f2.read())

print("Files merged successfully into 'merged.txt'.")

