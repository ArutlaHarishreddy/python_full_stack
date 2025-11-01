#Implement a decorator that counts how many times a function is called.
def function_calling_count(greet):
    def wrapper(*args,**kwargs):
        wrapper.count+=1
        print(f"Function {greet.__name__} called {wrapper.count} times")
        return greet(*args,**kwargs)
    wrapper.count=0
    return wrapper
@function_calling_count
def greet(name):
    print(f"Hello {name}")

greet("Harish")
greet("Name")
greet("Ashish")