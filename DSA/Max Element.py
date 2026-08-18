#Max Element
n=[1,3,2,78,4,9]
maxi=n[0]
for num in n:
    if num>maxi:
        maxi=num
print(maxi)

#another method
n=max(n)
print(n)