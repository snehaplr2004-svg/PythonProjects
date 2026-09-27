#Write a program to create a list of 5 random 3 digit numbers

#from random import randint
# new=[]
# for i in range(0,5):
#         new.append(randint(100,999))
# print(new)

#write a program to create a 5digit random otp number
#
# from random import randint
# otp = randint(10000, 99999)
# print(otp)

#write a program to find the position of a character in a string
# def posit(x,ch):
#     for i in range(len(x)):
#         if ch==x[i]:
#             print(i)
#


# x=input("Enter a string")
# ch=input("Enter the character")
# posit(x,ch)
###########
# if ch in s:
#     print(s.index(ch))
# else:
#     print("Not found")

#define a function that takes a string as argument and returns a new dictionary
#where keys are character and values are count of each charcter

# def fun(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i] = d[i] + 1
#         else:
#             d[i] = 1
#     return d
# s=input("Enter a string")
# a=fun(s)
# print(a)

##############
#
# def fun(s):
#     new={}
#     for i in s:
#         new[i]=s.count(i)
#     return new
# a=fun("hello")
# print(a)

#Define a function that takes string as argument and print the count of
# digits,spaces,letters in that string
# def fun(s):
#     letters = 0
#     digits = 0
#     spaces = 0
#     for i in s:
#         if i.isalpha():
#             letters = letters + 1
#         elif i.isdigit():
#             digits = digits + 1
#         elif i.isspace():
#             spaces = spaces + 1
#
#     print("Letters:", letters)
#     print("Digits:", digits)
#     print("Spaces:", spaces)
# s = input("Enter a string: ")
# fun(s)

#list built in function
# l=[1,7,4,6,9,2,3]
# l.append(5)
# print(l)
# l.extend([4,5,6])
# print(l)
# l.sort()
# print(l)
# l.reverse()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.pop()
# print(l)
# l.pop(1)
# print(l)
# l.insert(1,8)
# print(l)
# l.remove(6)
# print(l)
# l.clear()
# print(l)

#given list
#l=[1,2,2,3,4,4,5,6]
#create new dic where keys are num and values are num occurence of each value
# new={}
# for i in l:
#     new[i]=l.count(i)
# print(new)

#given list
l=[11,34,78,23,90,65]

                #find largest num
#print(max(l))

#or method

# l.sort()
# print(l[-1])
                #second largest
# l.sort()
# print(l[-2])

#or method

# l.remove(max(l))
# second_largest = max(l)
# print(second_largest)

                #smallest num
# s=min(l)
# print(s)

#second smallest
# l.remove(min(l))
# s=min(l)
# print(s)

# l=[['arun',23,30000],['amal',25,50000],['anu',27,40000]]
# #max salary
# maximum=max(i[2] for i in l)
# print(maximum)
#
# #minimum age
# minimum=min(i[1] for i in l)
# print(minimum)


# l=[23,45,67,12,90,78]
#
# # #find lar without built in
#
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print("maximun",max)
#
# #find smallest number without built in
#
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print("minimun",min)

    ######  SET
# s={1,2,3,4}
# s.add(5)
# print(s)
# s.update((6,7,8))
# print(s)
# s.remove(3)
# print(s)
# s.discard(4)
# print(s)
# s.pop()  #here 1st element got removed
# print(s)

# s={1,2,3}
# t={3,4,5}
# print(s.union(t))
# print(s.intersection(t))
# print(s.difference(t))
# print(s.symmetric_difference(t))

#l=[1,1,2,3,3,4]

# #remove duplicetes
#print(list(set(l)))

# l=[1,1,2,3,3,4]
#     #remove duplicates without using set()(order be preserved)
# new = []
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

# l1=[13,27,30,42,57]
# l2=[13,57,89,33,80]
# #find common element
# new=[]
# for i in l1:
#     if i in l2:
#        new.append(i)
# print(new)
#
#                 or method
#
# s1=set(l1)
# s2=set(l2)
# print(list(s1.intersection(s2)))

##      DICTIONARY
#
# d={'name':'ammu','age':23,'place':'df'}
#
# print(d.keys)

