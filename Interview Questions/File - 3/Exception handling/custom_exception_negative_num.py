#32. Create a custom exception `NegativeNumberError` and raise it when a negative number is passed.
class NegativeNumberError(Exception):
    pass
try:
    n=int(input("Enter any Number:"))
    if n<0:
        raise NegativeNumberError("Negative numbers are not allowed")
    else:
        print(f"{n} It is a Positive Number")
except NegativeNumberError as e:
    print("Error:",e)