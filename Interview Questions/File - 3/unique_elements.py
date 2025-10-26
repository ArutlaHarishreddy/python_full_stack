#Write a function that accepts a list and returns a new list with only unique elements.

def unique_elements(lst):
    unique_lst=[]
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
print(unique_elements([5,5,6,3,8,2,7,4,9,5,7,2,1]))