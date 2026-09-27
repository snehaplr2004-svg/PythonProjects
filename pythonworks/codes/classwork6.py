# # # Q1.Define a function that takes 2 numbers and returns their product
def product(a,b):
    p=a*b
    return p
n=product(2,3)
print("Product",n)

# # Q2.Define a function that takes a string and returns number of vowels
def vowel_count(a):
    c=0
    for i in a:
        if i in "aeiou":
            c+=1
    return c
s=input("Enter a string")
n=vowel_count(s)
print("Count of vowel",n)

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle

def area(x,y):
    a=x*y
    return a
l=int(input("enter length"))
b=int(input("enter breadth"))
n=area(l,b)
print("Area",n)

# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list

def newl(a):
    nl=[]
    for i in a:
        if i%2==0:
            nl.append(i)

    return nl

l=[45,78,90,12,35]
n=newl(l)
print(n)


# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
#     print(a) 6 12 3 21 8 17

def newl(a):
    nl=[]
    for i in a:
        s=0
        for j in str(i):
             s=s+int(j)
        nl.append(s)
    return nl

l = [123, 345, 111, 678, 134, 809]
n=newl(l)
print(n)

#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]
            #op 12 34 78 12 67 34 90 23

def newl(a):
    nl = []
    for i in a:
        if i not in nl:
            nl.append(i)
    return nl

l = [12, 34, 78, 12, 67, 34, 90, 23]
n = newl(l)
print(n)

#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]

        # a=fun(list1,list2)
        # print(a) 34 90
def fun(list1, list2):
    nl = []

    for i in list1:
        if i in list2:
            nl.append(i)

    return nl


list1 = [12, 34, 56, 78, 90]
list2 = [90, 34, 11, 57, 45]

a = fun(list1, list2)
print(a)
