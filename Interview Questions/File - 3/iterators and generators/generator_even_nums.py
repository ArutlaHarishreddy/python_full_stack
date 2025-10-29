#Write a generator function that yields even numbers up to `n`.
def even_numbers(n):
    for i in range(0,n+1,2):
        yield i
n=int(input("Enter any number:"))
for even in even_numbers(n):
    print(even)
    