# number=123
# string=str(number)
# print(type(string))

# stirng="123"
# number=int(stirng)
# print(type(number))

#list : List is an ordered and mutable after creation and it has square brackets[] and allows duplicates
#set : Set is Unordered and mutable after creation and it has paranthesis() and does not allows duplicates
#tuple : Tuple is Ordered and it is immutable after creation and allows duplicates and it has paranthesis().
#dict: Ordered and mutable after creation and it doesnot allows duplicates and it has {}curly braces.

#Swapping of two numbers
# a=10
# b=4
# a,b=4,10
# print(a)
# print(b)

# a=10
# b=5
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

#reverse of a number
# n=int(input("Enter any number:"))
# rev=0
# while n>0:
#     rem=n%10
#     n=n//10
#     rev=rev*10+rem
# print(rev)

# #palindrome
# n=int(input("Enter any number:"))
# Original=n
# rev=0
# while n>0:
#     rem=n%10
#     n=n//10
#     rev=rev*10+rem
# if Original==rev:
#     print("Palindrome")
# else:
#     print("Not Palindorme")

#checking a number is prime or not prime
# n=int(input("Enter any number:"))
# if n<2:
#     print("Not prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")

#printing prime numbers
# n=int(input("Enter any number:"))
# for num in range(2,n+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num,end=" ")

# counting prime numbers
# n=int(input("Enter any number:"))
# a=0
# for num in range(2,n+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         a=a+1
# print(n,"-->",a)

#printing fibonacci series
# n=int(input("Enter any number:"))
# a=0
# b=1
# for i in range(n):
#     print(a, end=" ")
#     c=a+b
#     a=b
#     b=c

#stars triangle
# rows=5
# for i in range(1,rows+1):
#     print(" "*(rows-i)+"* "*i)

# print("Another triangle")
# for i in range(1,rows+1):
#     print(" "*(rows-i)+"*"*(2*i-1))

#printing even numbers
# n=int(input("Enter any number:"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i, end=" ")

#filtering even numbers
# x=[1,2,3,4,5,6,7,8,9,10]
# for i in x:
#     if i%2==0:
#         print(i, end=" ")

#factorial
# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

#recursion factorial
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

#Reverese string
# text=input("Enter string:")
# reverse_string=""
# for char in text:
#     reverse_string= char+reverse_string
# print(reverse_string)

#counting vowels
# def count_vowels(text):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in text:
#         if char in vowels:
#             count = count +1
#     return count
# print(count_vowels("Harishreddy aeiou"))

#shallow copy
# import copy
# list=[[1,2],[3,4]]
# shallow_copy=copy.copy(list)
# shallow_copy[1][1]=99
# print(list)        #deep copy is opposite to the shallow copy

