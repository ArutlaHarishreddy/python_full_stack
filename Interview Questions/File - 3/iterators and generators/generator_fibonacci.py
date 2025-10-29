#Implement a generator that yields Fibonacci numbers.
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
n=int(input("Enter any number:"))
for val in fibonacci(n):
    print(val,end=" ")