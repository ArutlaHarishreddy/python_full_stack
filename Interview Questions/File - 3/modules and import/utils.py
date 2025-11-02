# Write code using `__name__ == "__main__"` to run tests only when executed directly.
def is_palindrome(text):
    cleaned=text.replace(" ","").lower()
    return cleaned==cleaned[::-1]

if __name__=="__main__":
    print("Runnig tests inside utils.py....")
    text_words=["madam","student","level","Harish"]
    for word in text_words:
        if is_palindrome(word):
            print(f"This {word} is a palindrome")
        else:
            print(f"This {word} is not palindrome")
                