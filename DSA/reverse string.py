#reverse string
text="Hello"
reverse=text[::-1]
print(reverse)

#another method
reversed_text=""
for char in text:
    reversed_text=char+reversed_text
print(reversed_text)

#join method
reversed_text="".join(reversed(text))
print(reversed_text)