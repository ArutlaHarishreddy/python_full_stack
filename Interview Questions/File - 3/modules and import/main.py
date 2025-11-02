#Write a script with two modules, import one into the other, and call a function.
import module1 # type:ignore
name=(input("Enter any name:"))
message=module1.greet(name)
print(message)