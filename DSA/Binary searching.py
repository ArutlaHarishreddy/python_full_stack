#Binary searching
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left <= right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return "Not Found"
arr=[10,20,30,40,50,60,70]
target=40
print(binary_search(arr,target))
            