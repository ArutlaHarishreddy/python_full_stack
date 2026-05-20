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

# #right aligned triangle
# rows=5
# for i in range(1,rows+1):
#     print(' '*(rows-i)+"*"*i)

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