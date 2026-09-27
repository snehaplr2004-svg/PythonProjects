# Create a database named shop
# Create a table `Product` with the following fields:
# * `product_id` – Primary Key
# * `name`
# * `brand`
# * `category`
# * `price`
# * `stock`

# Write a *menu-driven Python program using MySQL* with the following options:
# ```text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit

import mysql.connector

# con=mysql.connector.connect(user="root",password="root",host="localhost",use_pure=True)
# c=con.cursor()
# c.execute("Create database shop")
# print("Database file created")

con=mysql.connector.connect(user="root",password="root",host="localhost",database="shop",use_pure=True)
c=con.cursor()
# c.execute('''
# create table product(product_id int not null primary key,
#         name varchar(25),
#         brand varchar(30),
#         category varchar(25),
#         price int,
#         stock int)''')
# print("Table created successfully")

def insert():
    number=int(input("enter the product id"))
    name=input("enter name")
    brand=input("enter brand")
    category=input("enter category")
    price=int(input("enter price"))
    stock=int(input("enter stock"))

    query='insert into product(product_id,name,brand,category,price,stock)values(%s,%s,%s,%s,%s,%s)'
    data=(number,name,brand,category,price,stock)
    c.execute(query,data)
    con.commit()
    print("Data Inserted")
def readdb():
    query= "select * from product"
    c.execute(query)

    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("No records found")
def search():
    number=int(input("enter the product id"))
    query= "select * from product where product_id=%s"
    data=(number,)
    c.execute(query,data)

    record=c.fetchone()
    if record:
            print(record)
    else:
        print("No records found")
def update():
    number=int(input("enter productid"))
    stock=int(input("enter the new stock"))
    query= "update product set stock=%s where product_id=%s"
    data=(stock,number)
    c.execute(query,data)
    con.commit()
    print("updated")
def delete():
    number=int(input("enter the product id"))
    query= "delete from product where product_id=%s"
    data=(number,)
    c.execute(query,data)
    con.commit()
    print("deleted")
while (1):
    print(" 1. Insert Product details")
    print(" 2. Read all Product details")
    print(" 3. Search a Product by product_id")
    print(" 4. Update the stock of a Product")
    print(" 5. Delete a Product record")
    print(" 6. Exit")

    ch=int(input("Enter your choice:"))
    if ch==1:
        insert()
    elif ch==2:
        readdb()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        exit()
    else:
        print("Invalid Choice")