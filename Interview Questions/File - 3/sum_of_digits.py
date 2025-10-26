#Write a function that returns the sum of digits of a number.
def sum_of_digits(num):
    sum=0
    for i in range(num+1):
        sum=sum+i
    return sum
print(sum_of_digits(5))


