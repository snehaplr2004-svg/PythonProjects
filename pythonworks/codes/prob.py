#write a program to check user entered no is 2,3,4 digit

# n=int(input("Enter number: "))
# if 10<=n<=99:
#     print(f"{n} is 2 digit number")
# elif 100<=n<=999:
#     print(f"{n} is 3 digit number")
# elif 1000<=n<=9999:
#     print(f"{n} is 4 digit number")
# else:
#     print(f"{n} is not 2,3 or 4 digit number")

#write basic calculator program to perform arithmetic operator

# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# op=input("Enter your operation: ")
# if op=='+':
#     print("Sum is ",n1+n2)
# elif op=='-':
#     print("Subtraction is ",n1-n2)
# elif op=='*':
#     print("Product is ",n1*n2)
# else:
#     print("Quotient is ",n1/n2)

#write a program to print number of days in a month

# l1=['January','March','May','June','July','August','October','December']
# l2=['April','June','September','November']
# l3=['February']
# month=input("Enter the month")
# if month in l1:
#     print(f"{month} has 31 days")
# elif month in l2:
#     print(f"{month} has 30 days")
# elif month in l3:
#     print(f"{month} has 28 or 29 days")
# else:
#     print("Please enter a valid month")

#write program to print grades based on following
#91-100 grade A
# 81=90 B
# 71-80 C
# 61-70 D
# below 61 E
# m=int(input("Enter mark: "))
# if 91<=m<=100:
#     print("A Grade")
# elif 81<=m<=90:
#     print("B Grade")
# elif 71<=m<=80:
#     print("C Grade")
# elif 61<=m<=70:
#     print("D Grade")
# elif m<61:
#     print("E Grade")

#write program to check following
   # a number divisible by 2 and 3
    # a number divisible by 2 and not by 3
    #a number divisible by 3 and not by 2
    #a number not divisible by 2 and 3

# n=int(input("Enter number: "))
# if n%2==0:
#         print("Entered number is divisible by 2")
#         if(n%3)==0:
#             print("Entered number is divisible by 3")
#         else:
#             print("Entered number is not divisible by 3")
# else:
#         print("Entered number is not divisible by 2")
#         if(n%3)==0:
#             print("Entered number is divisible by 3")
#         else:
#             print("Entered number is not divisible by 3")

# n=int(input("Enter number: "))
# if n>=0:
#     print("The number is positive")
#     if n%2==0:
#         print("The number is even")
#     else:
#         print("The number is odd")
# else:
#     print("The number is negative")
#     if n%2==0:
#         print("The number is even")
#     else:
#         print("The number is odd")