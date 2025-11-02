# Write code to read a text file and count the number of words.
filename="example.txt"
try:
    with open(filename,"r",encoding="utf-8") as file:
        text=file.read()
        print(text)
        word=text.split()
        count=len(word)
        print(f"This file {filename} has {count} words")
except FileNotFoundError:
    print("Error: The file {filename} was not Found")
    

        