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
