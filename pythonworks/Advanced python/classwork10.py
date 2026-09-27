# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()

class Movie:
    def __init__(self):
        self.movie_name =input("Enter movie name: ")
        self.year=input("Enter year: ")
        self.language=input("Enter language: ")
        self.director=input("Enter director: ")
        self.rating=float(input("Enter rating: "))
    def display_details(self):
        print("Movie Name:", self.movie_name,"Year:",self.year,"Language:",self.language,
              "Director:",self.director,"Rating:",self.rating)
    def update_rating(self):
        self.rating=float(input("Enter rating: "))
        self.display_details()
m=Movie()
m.display_details()
m.update_rating()


# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes
# to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.

class Vehicle:
    def __init__(self):
        self.brand=input("Enter brand")
        self.model=input("Enter model")
        self.colour=input("Enter colour")
        self.year=input("Enter year")
    def display(self):
        print("Brand:",self.brand,"Model:",self.model,"Colour:",self.colour,"Year",self.year)

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.mileage=input("Enter mileage")
    def display(self):
        print("Car Details:")
        super().display()
        print("Mileage:",self.mileage)
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.cc=input("Enter cc")
    def display(self):
        print("Bike Details:")
        super().display()
        print("CC:",self.cc)
print("Enter car details")
c=Car()
c.display()
print("Enter bike details")
b=Bike()
b.display()