# Write a function to check if a string is a palindrome without using slicing.
def is_palindrome(word:str)->bool:
    left,right=0,len(word)-1
    while left<right:
        if word[left] != word[right]:
            return False
        left=left+1
        right=right-1
    return True
print(is_palindrome("harisirah"))
print(is_palindrome("madam"))
print(is_palindrome("Harish"))


#Normal Palindrome
n=int(input("Enter the number"))
original=n
rev=0
while n>0:
    rem=n%10
    n=n//10
    rev=rev*10+rem
print(rev)
if original==rev:
    print("Palindrome")
else:
    print("Not palindrome")
