#linear_search
arr=[3,52,5,87,34,2,88,7]
array=len(arr)
target=8
def linear_search(arr,target):
    for i in range(array):
        if i==target:
            return i
    return "Not Found"
print(linear_search(arr,target))

