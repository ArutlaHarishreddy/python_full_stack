#Write code to handle division by zero with try-except.
try:
    a=int(input("Enter numerator:"))
    b=int(input("Enter denominator:"))
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
