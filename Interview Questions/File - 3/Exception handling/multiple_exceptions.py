#34. Write code that handles multiple exceptions (e.g., `ZeroDivisionError`, `ValueError`).
try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number"))
    result=a/b
    print("Sucessfully done",result)
except ValueError:
    print("Error: You should enter number only")
except ZeroDivisionError:
    print("Error:you should not divide by zero")
