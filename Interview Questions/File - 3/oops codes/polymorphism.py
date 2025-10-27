#What is polymorphism? Write code showing a function that takes different object types.
class Dog:
    def sound(self):
        return "Bark"
class Cat:
    def sound(self):
        return "meow"
def make_sound(animal):
    print(animal.sound())

dog=Dog()
cat=Cat()

make_sound(dog)
make_sound(cat)
