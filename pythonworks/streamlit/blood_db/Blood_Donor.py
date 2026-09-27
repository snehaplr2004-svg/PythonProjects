# Blood Donor Management System using Python, MySQL and Streamlit
# Create a MySQL database named blooddb and create a table named donor to store blood donor details.
# The donor table should contain the following fields:
# id – Integer, Primary Key, Auto Increment
# name – Donor name
# bloodgroup – Blood group
# phone – Phone number, should be unique
# city – City
# last_donation – Date of last donation

# Create a Python class to perform database operations on the donor table.
# The class should contain methods to:
# Add a new donor
# Retrieve all donors
# Retrieve a donor using ID
# Update donor details
# Delete a donor using ID
# Create a Streamlit interface to perform these operations through a user-friendly interface.

import mysql.connector
class BloodDonor:
    def __init__(self):
        self.connection = mysql.connector.connect(user="root",password="root",
                                                  host="localhost",database="blooddb",use_pure=True)
        print(self.connection)
        self.cursor = self.connection.cursor()
        print("Successfully connected to database")
    def get(self):     #reading all rec
        query = "select * from donor"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return  records
        else:
            print("No records found")
    def post(self,name,bloodgroup,phone,city,last_donation):
        query ="insert into donor(name,bloodgroup,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
        data=(name,bloodgroup,phone,city,last_donation)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Data inserted successfully")
    def retrieve(self,id): #read specific rec
        query="select * from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            # print(record)
            return record
        else:
            return False
            # print("No records found")
    def put(self,id,name,bloodgroup,phone,city,last_donation):
        query="update donor set name=%s,bloodgroup=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data=(name,bloodgroup,phone,city,last_donation,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            # print("Data updated successfully")
            return True
        else:
            return False
            # print("No records found")
    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:      # if no updation rowcount is 0
            # print("Data deleted successfully")
            return True
        else:
            # print("No records found")
            return False
blood_instance=BloodDonor()
