#pass by reference(behaviour with mutable object)
def modify_list(my_list):
    my_list.append(4)
    print(f"Inside function:{my_list}")
my_list=[1,2,3]
modify_list(my_list)  #function calling
print(f"Outside funtion:{my_list}")     #the list is modified
