#Create a class `Car` that tracks the number of cars created using a **class variable**.
class Car:
    car_count=0
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
        Car.car_count=Car.car_count+1
    def display_info(self):
        print("Car:",self.brand,self.model)
    @classmethod
    def total_cars(cls):
        print("Total cars created:",cls.car_count)

car1=Car("Tesla","model S")
car2=Car("Benz","Mersidezz")
car3=Car("Tata","XUV")
car1.display_info()
Car.total_cars()


        