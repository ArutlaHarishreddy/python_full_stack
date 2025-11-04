# #Use `map()` to square all elements of a list.
# numbers=[1,2,3,4,5,6]
# squared_numbers=list(map(lambda x:x**2, numbers))
# print(squared_numbers)



# #Use `filter()` to extract only even numbers from a list.
# numbers=[1,2,3,4,5,6]
# even_numbers=list(filter(lambda x:x%2==0, numbers))
# print(even_numbers)



# #Use `reduce()` to find the product of all numbers in a list.
# from functools import reduce                      #we must use functools to reduce
# numbers=[1,2,3,4,5]
# product_numbers=reduce(lambda x,y:x*y, numbers)
# print(product_numbers)




# #Use a lambda function to sort a list of tuples by the second element.
# data=[(1,3),(3,2),(4,1),(1,5)]        #we are sorting using second element in the tuple
# sorted_data=sorted(data,key=lambda x:x[1])  
# print(sorted_data)




#Combine `map`, `filter`, and `reduce` to compute the sum of squares of even numbers.
#method-1
# from functools import reduce
# numbers=[1,2,3,4,5,6]
# square_even=reduce(lambda x,y:x+y, (map(lambda x:x*x, filter(lambda x:x%2==0, numbers))))
# print(square_even)

#method-2
from functools import reduce
numbers=[1,2,3,4,5,6]
even_num=filter(lambda x:x%2==0, numbers)
square_even=map(lambda x:x**2, even_num)
sum_square_even=reduce(lambda x,y:x+y, square_even)
print(sum_square_even)