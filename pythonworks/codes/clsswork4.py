#write a program to find BMI(Body Mass Index)
# BMI= weight in (kg)/ height**2 in (m)
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese
#import code

w=int(input("Enter body weight"))
h=int(input("Enter body height"))
bmi=w/(h**2)
print("Body Mass Index= ",bmi)
if bmi<=18.4:
    print("Underweight")
elif  18.5<= bmi<=24.9:
    print("The weight is normal")
elif 25.0<=bmi<=39.9:
    print("Overweight")
elif bmi>=40.0:
    print("Obese")
else:
    print("Invalid")


#2.# A toy vendor supplies three types of toys:
# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,
# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys,
# and electrical charging based toys respectively.
# Write a program that reads the product code and the order amount
# and prints out the net amount that the customer is required to pay after the discount.
        #code_1-battery_based
        # code_2-key_based
        # code_3-electrical_charging_based

code=int(input("Enter your code"))
price=int(input("Enter your price"))
if code==1:
    if price>=1000:
        d=price-(price*0.010)
        print("Discount",d)
    else:
        print("no discount")
elif code==2:
    if price>=1000:
        d=price-(price*0.05)
        print("Discount ",d)
    else:
        print("no discount")
elif code==3:
    if price>=500:
        d = price - (price * 0.010)
        print("Discount",d)
    else:
        print("no discount")
else:
    print("Invalid code")


#3 FIZZBUZZ Problem
# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

n=int(input("Enter the number"))
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print(n)