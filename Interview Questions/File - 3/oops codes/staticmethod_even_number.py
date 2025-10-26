#Implement a class with a **static method** to check if a number is even.
class Even_number:
    @staticmethod
    def is_even(num):
        return num%2==0
num=int(input("Enter any integer:"))
if Even_number.is_even(num):
    print(num,"is even")
else:
    print(num,"is odd")