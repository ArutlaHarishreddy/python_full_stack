#Implement a module with a helper function `is_palindrome()`, then import and test it.
def is_palindrome(text):
    cleaned=text.replace(" ","").lower()
    return cleaned==cleaned[::-1]
