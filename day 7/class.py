"""class Car:
    brand=" "
    model_name=" "
    year=0
    def __init__(self,brand,model_name,year):
        self.brand=brand
        self.model_name=model_name
        self.year=year
    def __str__(self):
        return f"the car is {self.brand}"
c=Car("bmw","m5",2025)
print(c.brand)
print(c)"""
"""class Company:
    name="bmw"
class Model:

    model="m5"
class Year(Company,Model):
    year=2025
c=Year()
print(c.name)
print(c.model)
print(c.year)"""
#method overriding
"""class Car:
    def brand(self):
        print("inside car")
class Bike(Car):
     def brand(self):
         print("inside bike")
         super().brand()
c=Bike()
c.brand()"""
#class overloading
"""class Sum:
    def add(self,a,b):
        return a+b
class A(Sum):
    def add(self,a,b,c=0):
        return a+b+c
a=A()
print(a.add(1,2,3))"""
#encapusulation
"""class Sum:
    _a=10
    def display(self):
        print(self._a)
class Sum1(Sum):
    def display(self):
        print(self._a)


b=Sum1()
b.display()
print(b._a)
#abstraction"""
"""from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def car(self):
        pass
    @abstractmethod
    def bike(self):
        pass
class Building(Vehicle):
    def car(self):
        pass
    def bike(self):
        print("bike")


#v=Vehicle()
#v.car( )
b=Building()
b.car()"""
