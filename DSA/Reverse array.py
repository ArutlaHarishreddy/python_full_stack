#Reverse array
n=[1,2,3,4,5,6,7,8,9]
n.reverse()
print(n)

#Two pointers method
num=[1,2,3,4,5,6]
left=0
right=len(num)-1
while left<right:
    num[left],num[right]=num[right],num[left]
    left=left+1
    right=right-1

print(num)