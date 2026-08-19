#Bubble sorting
def bubble_sorting(arr):
    n=len(arr)-1
    for i in range(n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr
arr=[6,4,2,8,5,1,3,7]
print(bubble_sorting(arr))
