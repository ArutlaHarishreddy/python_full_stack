# Implement a function that retries division 3 times if an error occurs.
def safe_divide(a,b):
    attempts=0
    while attempts<3:
        try:
            result=a/b
            print("Division Successful",result)
            return result
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
            b=int(input("Enter new denominator:"))
            attempts+=1
        except Exception as e:
            print("UnExcepted Error:",e)
            attempts+=1
    print("Failed after 3 attempts")
a=int(input("Enter numerator:"))
b=int(input("Enter Denominator:"))
safe_divide(a,b)

