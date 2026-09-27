# import mysql.connector
#     or
                    # from mysql import connector
# con=mysql.connector.connect(user="root",password="root",host="localhost",use_pure=True)
#      #establish connection btw python code and sql server
#      #it returns a connection object
# print(con)
#
# c=con.cursor()   #cursor object used to execute sql queries/commands
#
# # # c.execute(command)
# # # execute database file
# c.execute("Create database school_db")
# print("Database file created")

# con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db",use_pure=True)
# c=con.cursor()
# c.execute('''
# create table student(roll_no int not null primary key,
#         name varchar(25),
#         age int,
#         place varchar(25),
#         phone varchar(20),
#         total_mark int)''')
# print("Table created successfully")

# c.execute('''insert into student(roll_no,name,age,place,phone,total_mark)
#             values (101,'arun',11,'ekm',984536182,145),
#             (102,'amal',12,'ekm',573476478,140),
#             (103,'anu',11,'tvm',4637688642,147),
#             (104,'hari',12,'tcr',2564678474,144),
#             (105,'manu',11,'ekm',8753656859,141)
#             ''');
                #   OR
# query='insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)'
# data=(106,'Kiran',12,"ekm",355778889,140)
# c.execute(query,data)
#
# con.commit()  #to save data permanently into database
# print("Data Inserted")

            # READ OPERATION
# query= "select * from student"
# c.execute(query)
#
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("No records found")

                #read all attributes of a student with roll number =roll number entered by user
# number=int(input("enter the number"))
# query= "select * from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
#
# record=c.fetchone()
# if record:
#         print(record)
# else:
#     print("No records found")

            #update mark of a student with roll no =roll no entered by user
# number=int(input("enter the number"))
# mark=int(input("enter the new mark"))
# query= "update student set total_mark=%s where roll_no=%s"
# data=(mark,number)
# c.execute(query,data)
# con.commit()
# print("updated")

            #delete record with roll no=roll no entered by user
# number=int(input("enter the roll number"))
# query= "delete from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# con.commit()
# print("deleted")

            # create a new record using values entered by user
# number=int(input("enter the roll number"))
# name=input("enter name")
# age=int(input("enter age"))
# place=input("enter place")
# phone=input("enter phone number")
# total_mark=int(input("enter total marks"))
#
# query='insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)'
# data=(number,name,age,place,phone,total_mark)
# c.execute(query,data)
# con.commit()
# print("Data Inserted")

            # ***CLASS BASED***
#define a class to perform database operation on book table
#create a class named BookListCreateRetrieveUpdateDelete and define methods
#list()-->for reading all records
#create()-->for creating new record
#retrieve(id)-->for reading specific rec
# update(id,data)-->for updating specific rec
# delete(id)-->for deleting specific
#
# import mysql.connector
# class BookListCreateRetrieveUpdateDelete:
#     def __init__(self):
#         self.connection = mysql.connector.connect(user="root",password="root",
#                                                   host="localhost",database="library_db",use_pure=True)
#         print(self.connection)
#         self.cursor = self.connection.cursor()
#         print("Successfully connected to database")
#     def list(self):     #reading all rec
#         query = "select * from book"
#         self.cursor.execute(query)
#         records = self.cursor.fetchall()
#         if records:
#             for row in records:
#                 print(row)
#         else:
#             print("No records found")
#     def create(self,title,author,price,pages,language):
#         query ="insert into book(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"
#         data=(title,author,price,pages,language)
#         self.cursor.execute(query,data)
#         self.connection.commit()
#         print("Data inserted successfully")
#     def retrieve(self,id): #read specific rec
#         query="select * from book where id=%s"
#         data=(id,)
#         self.cursor.execute(query,data)
#         record=self.cursor.fetchone()
#         if record:
#             print(record)
#         else:
#             print("No records found")
#     def update(self,id,title,author,price,pages,language):
#         query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
#         data=(title,author,price,pages,language,id)
#         self.cursor.execute(query,data)
#         self.connection.commit()
#         if self.cursor.rowcount>0:
#             print("Data updated successfully")
#         else:
#             print("No records found")
#     def delete(self,id):
#         query="delete from book where id=%s"
#         data=(id,)
#         self.cursor.execute(query,data)
#         self.connection.commit()
#         if self.cursor.rowcount>0:      # if no updation rowcount is 0
#             print("Data deleted successfully")
#         else:
#             print("No records found")
# book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.list()
#
# # book_instance.create("Ennod","Nimna",400,200,"malayalam")
#
# # book_instance.retrieve(1)
# # book_instance.delete(3)
# # book_instance.update(1,"Dreams","Ravind",350,150,"engl")


#define a class to perform database operation on vehicle table
#create a class named VehicleListCreateRetrieveUpdateDelete and define methods
#list()-->for reading all records
#create(data)-->for creating new record
#retrieve(id)-->for reading specific rec
# update(id,data)-->for updating specific rec
# delete(id)-->for deleting specific
# table has id primary auto increment ,brand ,model,type,price,year

import mysql.connector
class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection = mysql.connector.connect(user="root",password="root",
                                                  host="localhost",database="vehicle_db",use_pure=True)
        print(self.connection)
        self.cursor = self.connection.cursor()
        print("Successfully connected to database")
    def list(self):     #reading all rec
        query = "select * from vehicle"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records found")
    def create(self,brand,model,type,price,year):
        query ="insert into vehicle(brand,model,type,price,year) values(%s,%s,%s,%s,%s)"
        data=(brand,model,type,price,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Data inserted successfully")
    def retrieve(self,id): #read specific rec
        query="select * from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("No records found")
    def update(self,id,brand,model,type,price,year):
        query="update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s"
        data=(brand,model,type,price,year,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("Data updated successfully")
        else:
            print("No records found")
    def delete(self,id):
        query="delete from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:      # if no updation rowcount is 0
            print("Data deleted successfully")
        else:
            print("No records found")
vehicle_instance = VehicleListCreateRetrieveUpdateDelete()
vehicle_instance.list()

# vehicle_instance.create("Suzuki","nault","pd-45",90000,2023)

# vehicle_instance.retrieve(2)
# vehicle_instance.delete(4)
# vehicle_instance.update(2,"Wolkenwagon","wolks","g-45",95000,2025)
