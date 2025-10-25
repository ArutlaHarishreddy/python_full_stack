#Write a function that takes \*args and \*\*kwargs and prints them separately.
def args_kwargs(*args, **kwargs):
    print("Positional arguments:",args)
    print("Keyword arguments:",kwargs)
args_kwargs(10, 20, 30, name="Harish", age=21, city="Hyderabad")
