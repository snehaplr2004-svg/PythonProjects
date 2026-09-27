#Write a program to check whether two entered numbers are equal or not
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if n1==n2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

# #Write a program to check whether two entered words are equal or not
w1=input("Enter first word")
w2=input("Enter second word")
if w1==w2:
    print("The words are equal")
else:
    print("The words are not equal")

# #Write a program to find the maximum of two numbers
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if n1>n2:
    print(f"{n1} is greater than {n2}")
else:
    print(f"{n2} is greater than {n1}")

# #write a program to check whether the entered character is vowel or not
ch=input("enter your character")
vowel=('a','e','i','o','u')
if ch in vowel:
    print(f"{ch} is a vowel")
else:
    print(f"{ch} is not a vowel")
# # #Write a program to check whether the entered country name contains word 'land'
country=(input("Enter the country name"))
if 'land' in country:
    print(f" Word Land in {country} ")
else:
    print("Not Land")

# #write a program to check whether the entered number is 3 digit or not
n=int(input("Enter  number: "))
if 100<=n<=999:
    print(f"{n} is three digit number")
else:
    print(f"{n} is not three digit number")


#write a program to check whether the entered string is  palindrome or
s=input("Enter  number: ")
if s==s[ ::-1]:
    print(f"{s} is palindrome")
else:
    print(f"{s} not palindrome")

#Write a program to check whether a number is present in given list
l=[23,67,12,90]
n=int(input("Enter  number: "))
if n in l:
    print(f"{n} is present in the list")
else:
    print(f"{n} is not present in the list")
# #Write a program to check whether a key is present in a dictionary or not
d={101:'Arun',102:'Amal',103:'Anu'}
key=int(input("Enter the key"))
if key in d:
    print("Key is in dictionary")
else:
    print("Key is not in dictionary")

#Write a program to check whether the given password is strong/weak(if length less than 8 weak)
pas =input("Enter the password")
if len(pas)>8:
    print("Enter password is strong")
else:
    print("Enter password is weak")

