# class Person:
#     def __init__(self,n,a):  #constructor method
#                              #used to initialize object properties
#         self.name = n
#         self.age = a
#     def show(self):
#         print(self.name,self.age)
#
# p1=Person('arun',23)
# p1.show()
# p2=Person('amal',25)
# p2.show()


### by passing i/p dynmically

# class Person:
#     def __init__(self):
#         self.name = input("Enter name:")
#         self.age = int (input("Enter age:"))
#     def show(self):
#         print(self.name,self.age)
#
# p1=Person()     #object p1 of class person
# p1.show()
# p2=Person()      #object p2 of Class Person
# p2.show()


#   define a class named employee with attributes empid,name,age,salary,designation and
# methods getsalary() and showpersondetails()

#
# class Employee:
#     def __init__(self):
#         self.empid=int(input("Enter Employee ID"))
#         self.name = input("Enter employee name:")
#         self.age = int (input("Enter age:"))
#         self.salary = int(input("Enter Employee salary:"))
#         self.designation = input("Enter Employee designation")
#
#     def showsalary(self):
#         print("Salary = ",self.salary)
#
#     def showpersondetails(self):
#         print("Employee name :",self.name,"Age",self.age)
#
# e=Employee()
# e.showsalary()
# e.showpersondetails()

#define class named student with attributes roll no,name,mark1,mark2,mark3  and methods display() to display roll no and total mark of a student
#create student object and call mathods

#
# class Student:
#     def __init__(self):
#         self.rollno=int(input("Enter Student roll no:"))
#         self.name = input("Enter name:")
#         self.mark1 = int(input("Enter mark1"))
#         self.mark2 = int(input("Enter mark2:"))
#         self.mark3 = int(input("Enter mark3"))
#
#     def display(self):
#         print("Roll number=",self.rollno,"Total marks=",self.mark1+self.mark2+self.mark3)
#
# s=Student()
# s.display()


#create class named book with attribute title,author ,price,pages,lang
#and method gettitle(),getauthor(),getprice()
# settitle(),setauthor(),setprice


# class Book:
#     def __init__(self):
#         self.title=input("Enter Book Title:")
#         self.author = input("Enter author name:")
#         self.price = int(input("Enter price of book"))
#         self.pages = int(input("Enter pages of book:"))
#         self.language = input("Enter language:")
#
#     def gettitle(self):
#         print("Book Title:",self.title)
#
#     def getauthor(self):
#         print("Book Author:",self.author)
#
#     def getprice(self):
#         print("Book Price:",self.price)
#
#     def settitle(self):
#         self.title=input("Enter Book Title:")
#         self.gettitle()
#
#     def setauthor(self):
#         self.author=input("Enter Author name:")
#         self.getauthor()
#
#     def setprice(self):
#         self.price=input("Enter Book Price:")
#         self.getprice()
# b=Book()
# b.gettitle()
# b.getauthor()
# b.getprice()
# b.settitle()
# b.setauthor()
# b.setprice()

#create a class named Account with attributes acctname , acctnumber,balance, and
# method withdraw(), deposit(), showbalance()
# create account object and call mathod

# class Account:
#     def __init__(self):
#         self.acctname=input("Enter Account Name:")
#         self.acctnumber = int(input("Enter account number:"))
#         self.balance = int(input("Enter account balance:"))
#
#     def withdraw(self):
#         amount=int(input("Enter amount to withdraw:"))
#         if amount>self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance-=amount
#             self.showbalance()
#
#     def deposit(self):
#         deposit=int(input("Enter amount to deposit :"))
#         self.balance+=deposit
#         self.showbalance()
#
#     def showbalance(self):
#         print("Current Balance :",self.balance)
#
# a=Account()
# a.withdraw()
# a.deposit()
#
# a.showbalance()

##           by using list model to retrieve information

# class Account:
#     def __init__(self):
#         self.acctname=input("Enter Account Name:")
#         self.acctnumber = int(input("Enter account number:"))
#         self.balance = int(input("Enter account balance:"))
#
#     def showbalance(self):
#         print("Current Balance :",self.balance)
#
# a1=Account()
# a2=Account()
# l=[a1,a2]
# for i in l:
#     print(i.acctname)
#     i.showbalance()

##   BANKING OPERATION MENU DRIVEN USING class
# 1 create new acc
# 2 withdraw
# 3 deposit
# 4 show balance

# class Account():
#     def __init__(self):
#         self.acctname = input("Enter Account Name:")
#         self.acctnumber = int(input("Enter account number:"))
#         self.balance = int(input("Enter account balance:"))
#
#         def withdraw(self):
#             amount=int(input("Enter amount to withdraw:"))
#             if amount>self.balance:
#                 print("Insufficient balance")
#             else:
#                 self.balance-=amount
#                 self.showbalance()
#
#         def deposit(self):
#             deposit=int(input("Enter amount to deposit :"))
#             self.balance+=deposit
#             self.showbalance()
#
#         def showbalance(self):
#             print("Current Balance :",self.balance)
# l=[]
# while(1):
#     print("1.Create Account")
#     print("2.Withdraw ")
#     print("3.Deposit ")
#     print("4.Show Balance")
#     print("5.Exit")
#
#     ch=int(input("Enter your choice: "))
#
#     if ch==1:
#         a=Account()
#         l.append(a)
#         print(l)
#     elif ch==2:
#         number=int(input("Enter account number:"))
#         for i in l:
#             if i.acctnumber==number:
#                 i.withdraw()
#                 break
#         else:
#             print("Account doesnot exist")
#     elif ch==3:
#         number = int(input("Enter account number:"))
#         for i in l:
#             if i.acctnumber == number:
#                 i.deposit()
#                 break
#         else:
#             print("Account doesnot exist")
#     elif ch==4:
#         number = int(input("Enter account number:"))
#         for i in l:
#             if i.acctnumber == number:
#                 i.showbalance()
#                 break
#         else:
#             print("Account doesnot exist")
#     else:
#         exit()



# class Account():
#     def __init__(self):
#         self.acctnumber = int(input("Enter account number:"))
#         self.acctname = input("Enter Account name:")
#         self.balance = int(input("Enter balance:"))
#
#     def withdraw(self):
#         x=int(input("enter amount to be withdrawn:"))
#         if x<self.balance:
#             self.balance=self.balance-x
#             self.showbalance()
#         else:
#             print("Insufficient balance to withdraw")
#
#     def deposit(self):
#         x = int(input("enter amount to be deposited:"))
#         self.balance = self.balance + x
#         self.showbalance()
#
#     def showbalance(self):
#         print("Balance is",self.balance)
#
# l=[]
# while (True):
#             print("Menu Driven Operations")
#             print('1.Create an account')
#             print('2.Withdraw')
#             print('3.Deposit')
#             print('4.Show Balance')
#             print('5.Exit')
#
#
#             ch = int(input("Enter the choice:"))
#             if ch == 1:
#                 a=Account()
#                 l.append(a)
#
#             elif ch == 2:
#                  number=int(input("Enter account number:"))
#                  for i in l:
#                      if(i.acctnumber==number):
#                          i.withdraw()
#                          break
#                  else:
#                         print("Account does not exist")
#             elif ch == 3:
#                 number = int(input("Enter account number:"))
#                 for i in l:
#                     if (i.acctnumber == number):
#                         i.deposit()
#                         break
#                 else:
#                        print("Account does not exist")
#             elif ch == 4:
#                 number = int(input("Enter account number:"))
#                 for i in l:
#                     if (i.acctnumber == number):
#                         i.showbalance()
#                         break
#                 else:
#                         print("Account does not exist")
#                 pass
#
#             else:
#                 exit()








# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class Student():
    def __init__(self):
        self.roll = int(input("Enter roll number:"))
        self.name = input("Enter student name:")
        self.marks = int(input("Enter marks:"))

    def update(self):
        self.marks = int(input("Enter new marks:"))
        print("Marks updated successfully")

    def display(self):
        print("Roll Number:", self.roll)
        print("Name:", self.name)
        print("Marks:", self.marks)

l = []
while(1):

    print("\nMenu Driven Operations")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All Student Details")
    print("4. Search Student by Roll Number")
    print("5. Delete Student")
    print("6. Exit")

    ch = int(input("Enter the choice:"))
    if ch == 1:
        a = Student()
        l.append(a)
    elif ch == 2:
        number = int(input("Enter roll number:"))
        for i in l:
            if(i.roll == number):
                i.update()
                break
        else:
            print("Student does not exist")
    elif ch == 3:
        if len(l) == 0:
            print("No students found")
        else:
            for i in l:
                i.display()
    elif ch == 4:
        number = int(input("Enter roll number:"))
        for i in l:
            if(i.roll == number):
                print("Student Found")
                break
        else:
            print("Student does not exist")
    elif ch == 5:
        number = int(input("Enter roll number:"))
        for i in l:
            if(i.roll == number):
                l.remove(i)
                break
        else:
            print("Student does not exist")
    else:
        exit()
