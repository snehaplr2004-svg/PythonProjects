# class Parent:
#     def m1(self):
#         print("In parent class method 1")
#     def m2(self):
#         print("In parent class method 2")
#
# class Child(Parent):
#     def m3(self):
#         print("In child class method 3")
#     def m1(self):
#         print("In child class method 1")  #method overriding
#         super().m1()
# c=Child()
# c.m1()
# c.m2()
# c.m3()


#   ***SINGLE LEVEL INHERITANCE
#create parent class person that contain attributes name,age and method show to display that
#create a child class student with additional attribusted roll no and mark and display all
# child need method update mark for mark updation

# class Person:
#     def __init__(self):
#         self.name = input("Enter your name:")
#         self.age = int(input("Enter your age:"))
#     def show(self):
#         print("Name: ",self.name,"Age:",self.age)
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno =int(input("Enter your roll no:"))
#         self.mark = int(input("Enter your marks:"))
#     def show(self):
#         super().show()
#         print("Roll no:",self.rollno,"Marks:",self.mark)
#     def updatemark(self):
#         self.mark=int(input("Enter your marks:"))
#         self.show()
# s=Student()
# s.show()
# s.updatemark()



# class Category:
#     def __init__(self):
#         self.category_name = input("Enter category name:")
#     def show_category(self):
#         print("Category Name: ",self.category_name)
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name = input("Enter product name:")
#         self.price =int(input("Enter price of product:"))
#         self.quantity= int(input("Enter quantity of product:"))
#     def total_price(self):
#         print("Total price :",self.price*self.quantity)
# p=Product()
# p.show_category()
# p.total_price()

# define class company with attributes company_name and loc and method display company
# derive employee class from company with attributes empname, empid and salary

# class Company:
#     def __init__(self):
#         self.company_name = input("Enter company name:")
#         self.location = input("Enter location:")
#     def display_company(self):
#         print("Company Name: ",self.company_name,"Location:",self.location)
#
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.empid =int(input("Enter employe id:"))
#         self.empname =input("Enter employee name:")
#         self.salary =int(input("Enter salary:"))
#     def display_details(self):
#         super().display_company()
#         print("Employee id:",self.empid,"Employee name:",self.empname,"Salary:",self.salary)
#     def update_salary(self):
#         self.salary+=self.salary*.10       #or   self.salary=self.salary*1.10
#         self.display_details()
# e=Employee()
# e.display_details()
# e.update_salary()

#  MULTIPLE INHERITANCE

#create a class hospital with attributes hos_name,location,phn and methods display_hospital()

# class Hospital:
#     def __init__(self):
#         self.hos_name = input("Enter hospital name:")
#         self.location = input("Enter location of hospital:")
#         self.phon=input("Enter phone number:")
#     def display_hospital(self):
#         print("Hospital Name: ",self.hos_name,"Location:",self.location,"Phn Number:",self.phon)
#
# class Department:
#     def __init__(self):
#         self.dept_name = input("Enter department name:")
#         self.doctor_name = input("Enter doctor name:")
#     def display_department(self):
#         print("Departmant Name: ",self.dept_name,"Doctor name:",self.doctor_name)
#
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.patient_name =input("Enter patient name:")
#         self.age =int(input("Enter age of patient:"))
#         self.gender =input("Enter gender of patient:")
#         self.phone =int(input("Enter phn no of patient:"))
#         self.admission_date=input("Enter admission date of patient:")
#         self.bed_no=input("Enter bed no of patient:")
#         self.discharge_date=""
#     def set_discharge(self):
#         self.discharge_date=input("Enter discharge date of patient:")
#     def full_summary(self):
#         print("Patient Summary")
#         Hospital.display_hospital(self)
#         Department.display_department(self)
#         print("Patient name:",self.patient_name,"Age of patient:",self.age,"Gender:",self.gender,"Phn no:",self.phone,
#               "Admission date:",self.admission_date,"Bed Number:",self.bed_no)
#         if(self.discharge_date==""):
#             print("not yet discharged")
#         else:
#             print("Discharge date of patient:",self.discharge_date)
# p=Patient()
# p.full_summary()
# p.set_discharge()
# p.full_summary()

# method ovreloading

# class A:
#     def f(self):
#         print("In first function f")
#     def f(self,a):
#         print("In second function f")
#     def f(self,a,b):
#         print("In third function f")
# a=A()
#     # a.f()  #here 2 arg missing error
#     # a.f(10) #1 arg missing error
# a.f(10,20)

#create an abstract class shape with abstract methods get_area() and get_perimeter()
# create 2 sub class reactangle,square
#each class should calculate area() and perimeter() differently

# from abc import ABC,abstractmethod
# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self):
#        self.length=int(input("Enter length"))
#        self.breadth=int(input("Enter breadth"))
#
#     def get_area(self):
#         print("Area of Rectangle:",self.length*self.breadth)
#     def get_perimeter(self):
#         print("Perimeter of Rectangle:",2*(self.length+self.breadth))
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
#
# class Square(Shape):
#     def __init__(self):
#         self.side = int(input("Enter side of square"))
#
#     def get_area(self):
#         print("Area of Square:",self.side**2)
#
#     def get_perimeter(self):
#         print("Perimeter of Square:",4*self.side)
#
# s=Square()
# s.get_area()
# s.get_perimeter()

# create abstract class Employee and has method calculate_salary()
# create 2 subclass fulltimeEmployee and HalftimeEmployee with common attributes empid empname and age
#fulltimeEmploye has additional attributes monthlysalary and
# halftimeEmployee has additional attributes time and rate
#calculate salary for each differently

# from abc import ABC,abstractmethod
# class Employee(ABC):
#
#     def __init__(self):
#         self.empid=int(input("Enter employee id"))
#         self.name=input("Enter employee name")
#         self.age=int(input("Enter employee age"))
#
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class FulltimeEmployee(Employee):
#     def __init__(self):
#         super().__init__()
#         self.monthly_salary=int(input("Enter salary"))
#
#     def calculate_salary(self):
#         print("Salary:",self.monthly_salary)
# 
# class HalftimeEmployee(Employee):
#     def __init__(self):
#         super().__init__()
#         self.hours = int(input("Enter hours of working"))
#         self.rate=int(input("Enter rate of working"))
#
#     def calculate_salary(self):
#         print("Salary:",self.hours * self.rate)
#
# f=FulltimeEmployee()
# f.calculate_salary()
#
# h=HalftimeEmployee()
# h.calculate_salary()
