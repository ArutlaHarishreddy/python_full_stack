#Create a generator that yields prime numbers up to n.
def prime_number(n):
    for num in range(2,n+1):
        for i in range(2, int(num ** 0.5)+1):
            if num%i==0:
                break
        else:
            yield num

n=int(input("Enter a Number:"))
for prime in prime_number(n):
    print(prime,end=" ")