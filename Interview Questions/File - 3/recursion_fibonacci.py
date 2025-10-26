#18. Implement a recursive function to compute Fibonacci numbers.
def fibonacci(n):
    if n<=0:
        return "Invalid Input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number"))
print(fibonacci(n))

#recursion fibonacci