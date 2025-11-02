#Write a script that imports a standard library (like `math`) and uses at least 3 functions.
import math
num=float(input("Enter a number:"))
square_root=math.sqrt(num)
power=math.pow(num,3)
sine_value=math.sin(math.radians(num))

print(f"square root of {num} = {square_root}")
print(f"power of a {num} = {power}")
print(f"Sine of {num} = {sine_value}")