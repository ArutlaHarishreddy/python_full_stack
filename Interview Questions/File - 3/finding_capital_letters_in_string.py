#Write code to find all words that start with a capital letter in a string.

text="My name is HARISH REDDY arutlA"
capitals=[]
for letter in text.split():
    if letter[0].isupper():
        capitals.append(letter)
print(capitals)