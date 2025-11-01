#Write a decorator that logs the execution time of a function.
import time
def log_execution_time(slow_function):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        print(start_time)
        result=slow_function(*args,**kwargs)
        end_time=time.time()
        print(end_time)
        print(f"Function {slow_function.__name__} executed in {end_time-start_time:.4f} seconds")
        return result
    return wrapper
@log_execution_time
def slow_function():  #it is like log_execution_time(slow_function)
    print("Running slow function")
    time.sleep(2)
    print("Done")
slow_function()