from typing import Any


class Person:
    def __init__(self, firstName, lastName, birthYear) -> None:
        self._birth_year = birthYear
        self.first_name = firstName
        self.last_name = lastName
        self.full_name = self.first_name+" "+self.last_name
        self._base_salary = 50000
        self._bonus = 10

    @property
    def salary(self):
        return int(self._base_salary * (1+self._bonus/100))

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, sal):
        self._base_salary = sal

    @property
    def age(self):
        return 2024-self._birth_year

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, fullName: str):
        self.first_name = fullName.split()[0]
        self.last_name = fullName.split()[1]

    def set_birth_year(self, year):
        self._birth_year = year


class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @property
    def diameter(self):
        return 2*self._radius


class Vehicle:
    vehicle_count = 0

    def __init__(self, company, model, year) -> None:
        self._company = company
        self._model = model
        self._year = year
        Vehicle.vehicle_count+=1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count
    
    @staticmethod
    def classify_vehicle(str):
        return "This is a "+str


class ElectricVehicle(Vehicle):

    @staticmethod
    def classify_vehicle(str):
        return "This is an electric " + str


class DynamicClass:
    def dynamic_attr(self, attrName, attrValue):
        setattr(self, attrName, attrValue)


class ValidatedAttribute:
    def __init__(self) -> None:
        self._value = None

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        if val<0:
            raise ValueError()
        else:
            self._value = val
    
