#define a fun to display "hello your name"
# def display_name():
#     n=input("enter your name:")
#     print("hello",n)
#     return
# display_name()

# #to find factorial
# def fact():
#     n=int(input("enter number:"))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print("Factorial",f)
#     return
# fact()
#
#count of given character in string
# def count_ch():
#     count=0
#     s=input("enter string:")
#     c = input("enter character:")
#     for i in s:
#         if (i==c):
#             count+=1
#     print(count)
#     return
# count_ch()

#num prime or not
# def check_prime():
#     n=int(input("enter number:"))
#     if (n>1):
#         for i in range(2,n):
#             if (n%i==0):
#                 print("Not prime")
#                 break
#         else:
#             print("Prime")
#     else:
#         print("neither Prime nor Composite")
#     return
# check_prime()

#def fun to find factors of a num
# def facto():
#     "Factors of a number"
#     n=int(input("enter number:"))
#     for i in range(1,n+1):
#         if (n%i==0):
#             print(i)
#     return   #to execute
# facto()

#########BY USING PARAMETER AND ARGUMENNTS

#sum of numbers
# def addi(n1,n2):
#     s=n1+n2
#     print("sum",s)
# addi(45,10)

#def funct that take amount,years,rate as 3 arguments and find si
# def simple(p,n,r):
#     s=(p*n*r)/100
#     print("Simple Interest",s)
#     return
#
# a=int(input("enter the amount"))
# y=int(input("enter the years"))
# r=int(input("enter the rate"))
#
# simple(a,y,r)

#def fun that takes 2 num as arg and return sum as result
# def add(a,b):
#     s=a+b
#     return s
# n=add(23,34)
# print("Sum",n)

#define function that take string as arg and return new dict where keys are words and values are len of word
# call fun and print dict
#
# def new_dict(n):
#      d={i:len(i) for i in n.split()}
#      return d
# s="python coding is easy and fun"
# a=new_dict(s)
# print(a)

#######or method without func
# new={}
# for i in s.split():
#       new[i]=len(i)
# print(new)

#def function take num as arg and check whether num is spy num or not
#eg: ie sum of digit=product of digit   22=2+2=2*2      ,1124

# def spy_num(n):
#     s=0
#     p=1
#     for i in str(n):
#         s=s+int(i)
#         p=p*int(i)
#     if s==p:                                  sample idea
#       return 0
#     else:
#       return 1
# d=int(input("Enter number"))
# a=spy_num(d)
# print(a)


# def spy_num(n):
#     s=0
#     p=1
#     for i in str(n):
#         s=s+int(i)
#         p=p*int(i)
#     if s==p:
#       print("Spy Number")
#     else:
#         print("Not Spy Number")
#     return
# d=int(input("Enter number"))
# spy_num(d)


# def fun(*args):
#      print(args)
# fun(23,"arun")

#def fun to fing sum of num using arbitary arg type
# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print("Sum=",sum)
#     pass
# add(10,20)
# add(1,2,3,4)

