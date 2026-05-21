#pass by value(behaviour with immutable objects)
def modify_number(num):
    num+=50
    print(f"Inside function:{num}")
num=4
modify_number(num)
print(f"Outside function:{num}")