#Implement a module with a helper function `is_palindrome()`, then import and test it.
from helper import is_palindrome # type: ignore
word=input("Enter any word:")
if is_palindrome(word):
    print(f"✅ {word} is a palindrome")
else:
    print(f"❌ {word} is not a palindrome")

    