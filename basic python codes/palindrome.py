n=int(input("Enter any number:"))
original=n
rev=0
while n>0:
    rem=n%10
    n=n//10
    rev=rev*10+rem
print(rev)
if original==rev:
    print("Is Palindrome")
else:
    print("Not a Palindrome")

