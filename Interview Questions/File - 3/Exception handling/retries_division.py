# Implement a function that retries division 3 times if an error occurs.
def safe_division(a,b):
    attempts=0
    while attempts<3:
        try:
            result=a/b
            print("Successfully divided", result)
            return result
        except ZeroDivisionError:
            print("Error: 0 is Not allowed to divide")
            attempts+=1
            b=int(input("Enter new Denominator:"))
            
        except Exception as e:
            print("Unexcepted Error", e)
            attempts+=1
    print("Failed after 3 attempts")
a=int(input("Enter Numerator:"))
b=int(input("Enter Denominator:"))
safe_division(a,b)  


