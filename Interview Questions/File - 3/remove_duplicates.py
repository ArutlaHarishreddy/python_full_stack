#Given a list of numbers, remove all duplicates **without using set()**.
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
nums=[1,1,3,2,2,4,5,6,5,7]
print(remove_duplicates(nums))



#using set()
def remove_duplicate(lst):
    return set(lst)
lst=[1,1,3,2,2,4,5,6,5,7]
print(remove_duplicate(lst))