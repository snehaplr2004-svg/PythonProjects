# sample demonstration to try and except

# def file_read():
#     try:
#         filename = input("Enter file name:")
#         f = open(filename, "r")
#         s = f.read()
#         print(s)
#         f.close()
#     except:
#         print("File not found")
#
# while(1):           #while(True) also correct
#     print("menu driven file operation")
#     print("1.file read")
#     print("2.file write")
#     print("3.file append")
#     print("4.file search")
#     print("5.file delete")
#     print("6.exit")
#
#     ch=int(input("Enter your choice:"))
#     if ch==1:
#         file_read()
#     elif ch==2:
#         pass
#     elif ch==3:
#         pass
#     elif ch==4:
#         pass
#     elif ch==5:
#         pass
#     else:
#         exit()

# eg to catch zero division error demonstration with try,except,else and finally

# try:
#     n1=int(input("Enter first number:"))
#     n2=int(input("Enter second number:"))
#     r=n1/n2
# except:
#     print("Zero division error")
# else:
#     print("Result",r)
# finally:
#     print

# applying multiple exception block

# try:
#     n1=int(input("Enter first number:"))
#     n2=int(input("Enter second number:"))
#     r=n1/n2
# except ZeroDivisionError:
#     print("Zero division error")
# except ValueError:
#     print("Value error")
# except:
#     print("error")
# else:
#     print("Result",r)
# finally:
#     print("Done")


# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# while True:
#     try:
#         from math import factorial
#         n=int(input("Enter number:"))
#         f=factorial(n)
#         print("Factorial",f)
#         break
#     except ValueError:
#          print("Value Error")
#     else:
#         pass


#or method

# def fact():
#     try:
#         from math import factorial
#         n=int(input("Enter number:"))
#         f=factorial(n)
#         print("Factorial",f)
#     except ValueError as e:
#          print(e)
#          print(type(e))
#          fact()
#     except Exception as e:
#         print(e)
#     else:
#         pass
# fact()
# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# # and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# while True:
#     try:
#         print('1.Addition')
#         print('2.Subtraction')
#         print('3.multiplication')
#         print('4.Division')
#         print('5.exit')
#
#         n = int(input("Enter choice"))
#         if n in [1,2,3,4]:
#             n1 = int(input("Enter number"))
#             n2 = int(input("Enter number"))
#
#             s=n1+n2
#             d=n1-n2
#             m=n1*n2
#             q=n1/n2
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Invalid Input")
#     except:
#         print("Error")
#     else:
#
#         if n == 1:
#                 print('Result', s)
#         elif n == 2:
#                 print("Result", d)
#         elif n == 3:
#                 print("Result", m)
#         elif n == 4:
#                 print("Result", q)
#         else:
#             exit()

#     OR

# try:
#     n1=int(input("Enter first number:"))
#     n2=int(input("Enter second number:"))
#     op=input("Enter the operation to be performed:")
#
#     if op=='+':
#         r=n1+n2
#     elif op=='-':
#         r=n1-n2
#     elif op=='*':
#         r=n1*n2
#     elif op=='/':
#         r=n1/n2
#     else:
#         print("Invalid Operation")
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Zero Division Error")
# except:
#     print("Error")
# else:
#     print("Result",r)
# finally:
#     print("Operation done successfully")

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not exist

# try:
#     filename=input("Enter File name")
#     f=open(filename,'r')
#     s=f.read()
#     print(s)
#     f.close()
# except FileNotFoundError:
#     print("File Does not exist")

#Given a Dictionary
# d={"name":"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

# d={"name":"arun","age":23,"place":"ekm"}
# try:
#     key=input("Enter Key")
#     print(d[key])
# except KeyError:
#     print("Key Does not exist")

#or
# except:
#     print("Key not exist")

# example to manually produce exception
# try:
#     n=int(input("enter a number"))
#     if n<10:
#         raise ValueError("Not eligible for scholorship")
#     else:
#         print("Eligible for scholorship")
# except ValueError as e:
#         print(e)
#

#to create an exception manually
# class MyException(Exception):
#     pass
# try:
#     n = int(input("enter a number"))
#     if n < 10:
#         raise MyException("Not eligible for scholorship")
#     else:
#         print("Eligible for scholorship")
# except MyException as e:
#     print(e)

#ask a user to enter a num .if num less than or equal to 0
# raise a valueerror with message "number must be positive"
#
# try:
#     n=int(input("enter a number"))
#     if n<=0:
#         raise ValueError("Number must be positive")
#     else:
#         print(n")
# except ValueError as e:
#     print(e)

#ask user to enter password.if its length is less than 8 character
# raise customexception InvalidPasswordError with the message ("Password should be 8
# characters")

# class InvalidPasswordError(Exception):
#     pass
# try:
#     password=input("enter password")
#     if len(password)<8:
#         raise InvalidPasswordError("Password should be 8 characters")
#     else:
#         print(password)
# except InvalidPasswordError as e:
#     print(e)

#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

# class InsufficientBalanceError(Exception):
#     pass
# try:
#     amount=int(input("enter amount"))
#     balance=3000
#     if amount<balance:
#         raise InsufficientBalanceError("Not Enough Balance.Transaction Failed")
#     else:
#         print("Transaction Successful")
# except InsufficientBalanceError as e:
#     print(e)
