# a=123
# b=str(a)
# print(b)
# print(type(b))

# a="123"
# b=int(a)
# print(b)
# print(type(b))

# a=True
# b=int(a)
# print(b)
# print(type(b))

# a=0
# b=bool(a)
# print(b)
# print(type(b))

# char="A"
# ascii=ord(char)
# print(ascii)

#tuple
# tuple=(1,2,3,4,5)
# print(tuple)
# print(type(tuple))

# #list
# list=[1,2,"abc",2]
# list1=["a","b"]
# print(list1)
# print(list)
# print(type(list))
# print(type(list1))

#swapping of two numbers
# a=10
# b=5
# a,b=b,a
# print(a)
# print(b)
#swapping without third variable
# a=5
# b=6
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

#right aligned triangle and middle triangle and left aligned triangle
# rows=5
# for i in range(1,rows+1):
#     print(' '*(rows-i)+"* "*i)

#reverse of a number
# n=int(input("Enter any number:"))
# rev=0
# while n>0:
#     rem=n%10
#     n=n//10
#     rev=rev*10+rem
# print(rev)

#prime number or not
# n=int(input("Enter any number:"))
# if n<2:
#     print("Not Prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print(n,"Not Prime")
#             break
#     else:
#         print("IS Prime")

#printing prime numbers
# n=int(input("Enter any number:"))
# for num in range(2,n+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)

#printing prime count
# n=int(input("Enter any number:"))
# count=0
# for num in range(2,n+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         count+=1
# print(n,":",count)

# #pass by value
# def modify_number(num):
#     num=num+50
#     print("Inside function:",num)
# num=3
# modify_number(num)
# print("Outside function:",num)

#pass by reference
# def modify_list(my_list):
#     my_list.append(4)
#     print("Inside function:",my_list)
# my_list=[1,2,3]
# modify_list(my_list)
# print("Outside function:",my_list)

#palindrome
# n=int(input("Enter any number:"))
# original=n
# rev=0
# while n>0:
#     rem=n%10
#     n=n//10
#     rev=rev*10+rem
# print(rev)
# if original==rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#nested for loop
# for over in range(1,20):
#     for ball in range(1,7):
#         print("overs:",over,".",ball)

#left aligned triangle
# row=5
# for i in range(1,row+1):
#     print("* "*i)

#printing fibonacci series
# n=int(input("Enter any number:"))
# a=0
# b=1
# for i in range(n):
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c

#stars triangles
# row=5
# for i in range(1,row+1):
#     print(" "*(row-i)+"* "*i)

#printing even numbers up to n
# n=int(input("Enter any number:"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,end=" ")

#even number
# n=int(input("Enter any number:"))
# if n%2==0:
#     print("Even")
# else:
#     print("Not even")

#filtering even numbers
# x=[1,2,3,4,5,6,7,8,9,10]
# for i in x:
#     if i%2==0:
#         print(i,end=" ")

#factorial
# n=int(input("Enter any number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact) 

#recursion 
# def fact(n):
#     if n<2:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

#reverse string 
text=input("Enter any string:")
reverse_string=" "
for char in text:
    reverse_string=char+reverse_string
print(reverse_string)

