# Write a program to print a multiplication table for a number.
n=int(input("Enter any number:"))
print("Multiplication table for",n)
for i in range(1,11):
    print(n,"x",i,"=",n*i)