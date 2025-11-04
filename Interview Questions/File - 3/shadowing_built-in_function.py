#49. Write a function with a variable that shadows a built-in function (e.g., `sum`) and fix it.

#wrong approach for shadowing built-in function

def good_function():
    total=10+20+30
    print(total)
good_function()
print(sum([1,2,3,4,5]))
def bad_function():
    global sum
    sum=10+20
    print(sum)
bad_function()
print(sum([1,2,3,4]))    #Error


