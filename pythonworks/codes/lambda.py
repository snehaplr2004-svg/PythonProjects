#def a fun that takes num as arg and return its sq call fun and print result

        #using user defined
# def square(n):
#     s=n*n
#     return s
#
# a=square(5)
# print(a)

       #using lambda
# a=lambda n:n*n
# print(a(5))

#sum of 2 num
# x=lambda a,b:a+b
# print(x(4,5))

#product of 3 num
# x=lambda a,b,c:a*b*c
# print(x(4,3,5))

#cube of a num
# x=lambda a:a**3
# print(x(4))

#first letter of string
# x=lambda a:a[0]
# print(x("hello"))

#length of string
# x=lambda a:len(a)
# print(x("hello"))

#reverse string
# x=lambda a:a[ ::-1 ]
# print(x("hello"))

#name value from dictionary
# x=lambda d:d['name']
# d={'name':'anuz','age':34}
# print(x(d))

#second element from list
# x=lambda a:a[1]
# print(x([10,20,30,40]))

#add 10 to a num
# x=lambda a:a+10
# print(x(5))

            ###HIGHER ORDER FUNCTIONS
        #BUILT IN HIGHER ORDER
    #MAP()

#create new list of sq
# n=[1,2,3,4]
# print(list(map(lambda x: x**2,n)))
# print(tuple(map(lambda x: x**2,n)))
# print(set(map(lambda x: x**2,n)))
# print(map(lambda x: x**2,n))

##create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda x: x**3,l)))

#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x: x**.5,l)))

#create a new list of lengths
#colors=['red','green','blue','yellow','black']
#print(list(map(lambda x: len(x), colors)))

#create a new list of first characters
#print(list(map(lambda x: x[0], colors)))

#create a new list of last characters
#print(list(map(lambda x: x[-1], colors)))

#create a new list of reverse of each elemnt
#print(list(map(lambda x: x[ ::-1], colors)))

#Given a list
l=[23,78,12,56]
#Add 10 to each element in the given sequence
# print(list(map(lambda x: x+10, l)))

#create a new list of reverse of each elemnt
# print(list(map(lambda x: int(str(x)[::-1]), l)))

##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # create a new list of emails
#print(list(map(lambda x: x['email'], l)))

#           filter
#l=[1,2,3,4,5,6,7,8,9,10]
#print(list(filter(lambda x: x%2==0,l)))

#l=[23,45,67,12,89,70]
#filter even value greater than 50
#print(list(filter(lambda x: x%2==0 and x>50,l)))

#colors=['red','green','blue','yellow','orange']
#color whose len > 5

#print(list(filter(lambda x: len(x)>5,colors)))

#filter colour containing letter n
#print(list(filter(lambda x:'n' in x,colors)))

            #REUDCE
# l=[1,2,3,4]
# #sum of lust using reduce

# import functools
# print(functools.reduce(lambda x,y:x+y,l,0))
# print(functools.reduce(lambda x,y:x*y,l,1))


