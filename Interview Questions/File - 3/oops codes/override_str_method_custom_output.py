#Override the `__str__` method in a class to display custom output.

class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def __str__(self):
        return f"{self.name}, {self.age} years old, Lives in {self.city}."
p1=Person("Harish",21,"Hyderabad")
print(p1)
    