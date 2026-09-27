#while

#1,2,3,...,100
# i=1
# while(i<=100):
#      print(i)
#      i=i+1

#1 3 5 7 ..15
# i=1
# while(i<=15):
#      print(i,end="")
#      i=i+2

#2 4 6 8...12
# i=2
# while(i<=12):
#      print(i)
#      i=i+2

#1 4 7 10 13 16
# i=1
# while(i<=16):
#      print(i)
#      i=i+3

#10 20 30 ..80
# i=10
# while(i<=80):
#      print(i)
#      i=i+10

#3  6 9 ..21
# i=1
# while(i<=7):
#      print(i*3)
#      i=i+1

#5 4 3 2 1
# i=5
# while(i>=1):
#      print(i)
#      i=i-1


#8 6 4 2 0
# i=8
# while(i>=0):
#      print(i)
#      i=i-2

# 100 101 102 ..200
# i=100
# while(i<=200):
#      print(i)
#      i=i+1

# print all 4 digit
# i=1000
# while(i<=9999):
#      print(i)
#      i=i+1

#print those num that are divisible by 3 in range (1,50)
# i=1
# while(i<=50):
#     if(i%3==0):
#         print(i,end=" ")
#     i=i+1
# print()

#3 digit num divisible by 5 and 7
# i=100
# while(i<=999):
#     if(i%5==0 and i%7==0):
#         print(i,end=" ")
#     i=i+1
# print()

#print num in range 100 and 200 that contain digit 3
#in operator works only in string
#also print count of those numbers
# i=100
# count=0
# while(i<=200):
#      s = str(i)
#      if '3' in s:
#         print(i)
#         count=count+1
#      i=i+1
# print()
# print("Count =",count)


######OR method

# i=100
# while(i<=200):
#     s=str(i)
#     if '3' in s:
#         print(i,end=" ")
#     i=i+1
# print()

#count those num divisible by 3 in range 1-50
# count=0
# i=1
# while i<=50:
#     if i%3==0:
#         print(i,end=" ")
#         count=count+1
#     i=i+1
# print()
# print("Count = ",count)
# print()

#sum of series 1 2 3 4 5
# sum=0
# i=1
# while (i<=5):
#     sum=sum+i
#     i=i+1
# print("Sum =",sum)

#product of series 1 2 3 4 5
# product=1
# i=1
# while (i<=5):
#     product=product*i
#     i=i+1
# print("Product =",product)

 #sum of first 10 even no
# sum=0
# product=1
# i=1
# while (i<=20):
#     sum=sum+i
#     product=product*i
#     i=i+2
# print("Sum =",sum)
# print("Product =",product)
#  #product of first 10 even no

# 4 9 14 19 24 29 34 39
# i=4
# while (i<=39):
#     print(i)
#     i=i+5
#872 0618 7946

#sum of series 1 3 5 7 9 11
# i=1
# sum=0
# while (i<=11):
#      sum=sum+i
#      i=i+2
# print(sum)

#product of no divisible by 3 and 5 in range 1 50
# i=1
# product=1
# while (i<=50):
#      if (i%3==0) and (i%5==0):
#          product=product*i
#      i=i+1
# print(product)

#count of 3 digit divisible by 7
# i=100
# count =0
# while (i<=999):
#      if (i%7==0):
#          count+=1
#      i=i+1
# print(count)

#factorial of number
# i=1
# n=int(input("Enter  number: "))
# fact=1
# while i<=n:
#     fact=fact*i
#     i=i+1
# print("Factorial = ",fact)

#multiplication table of a num (upto 10)
# i=1
# n=int(input("Enter number: "))
# while i<=10:
#     print(i,'*',n, '=',i*n)
#     i+=1

#FOR LOOP

# s="hello"
# for i in s:
#     print(i)

# l=['blue','red','green','yellow']
# for i in l:
#     print

# s={10,20,30,40}
# for i in s:
#     print(i)
#
# d={'a':10,'b':20,'c':30}
# for i in d:
#     print(i)
# for i in d.values():
#     print(i)

#given list l=[12 ,34 ,56 45 89 16 69 33
#print each num in list
#l=[12,34,56,45,89,16,69,33]
# for i in l:
#     print(i)

#print even num
# for i in l:
#     if i%2==0:
#         print(i)

#print num divisible by 5
# for i in l:
#      if i%5==0:
#          print(i)

# print num that contain digit 3
# for i in l:
#      if ('3' in str(i)):
#          print(i)

#given string s="hello world" ////////
#s="hello world"
#print each char
# for i in s:
#     print(i)

#print char that are not vowel
# vowel =["aeiouAEIOU"]
# for i in s:
#     if i not in vowel:
#         print(i)

#given dict
#d={'n1':23,'n2':46,'n3':89,'n4':24}

#print each value
# for i in d.values():
#     print(i)

#print odd value
# for i in d.values():
#     if (i%2!=0):
#         print(i)

#l={'red','green','orange','blue','black','yellow'}
#print each col
# for i in l:
#     print(i)

#col start with b
# for i in l:
#     if i[0]=='b':
#         print(i)

# print length greater than 5
# for i in l:
#     if len(i)>5:
#         print(i)

#l=[10,'arun','amal',35,3.6,6.9,89]
#print string val
# for i in l:
#     if type(i)==str:
#         print(i)

#print float val
# for i in l:
#     if type(i)==float:
#          print(i)

#l=[45,78,90,12,67]
#sum of list

# sum=0
# for i in l:
#     sum+=i
# print("Sum =",sum)

#product of even num

# product=1
# for i in l:
#     if i%2==0:
#         product*=i
# print("Product =",product)

#count of odd num

# count=0
# for i in l:
#     if i%2!=0:
#         count+=1
# print("Count=",count)

#RANGE

#1 2 3 4 5
#for i in range(1,6):
    # print(i)

#1 3 5 7 9
# for i in range(1,10,2):
#      print(i)

#2 4 6 8 10
# for i in range(2,11,2):
#      print(i)

#1 4 9 16 25
# for i in range(1,6):
#      print(i*i)

#4 9 14 19 24 29 34 39
# for i in range(4,40,5):
#      print(i)

#5 4 3 2 2 1
# for i in range(5,0,-1):
#      print(i)

# 8 6 4 2 0
# for i in range(8,-1,-2):
#      print(i)

#7 14 21 28 35 42
# for i in range(7,43,7):
#      print(i)

# #----OR------
# for i in range(1,7):
#      print(i*7)


#for loop-----------
#100 200 300  ....1000

# for i in range(100,1001,100):
#     print(i)

#1 8 27 64 125

# for i in range(1,6):
#      print(i**3)

#3 digit no divisible by 3

# for i in range(100,1000):
#     if i%3==0:
#         print(i)
#
# colours=['red','green','blue','yelloe','black']
# for i in colours:
#     print(i[ ::-1])

#print each digit in num
# n=1234
# for i in str(n):
#     print(i)

#sum of digit in num ie 1+2+3+4=10
# sum=0
# n=1234
# for i in str(n):
#     sum=sum+int(i)
# print(sum)

# given alist
l=[1,2,3,4]
#create a new list with sq of num
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)

#in list append used and in set add used to add elements
#create new set of same
#
# new=set()
# for i in l:
#     new.add(i**2)
# print(new)

#given strin
#s="hello world"
#create new string with only vowel
# new=""
# vowel='aeiou'
# for i in s:
#     if i in vowel:
#         new=new+i
# print(new)

# given a list
#l=[1,2,3,4]
#create new dict where keys are numbers and values are sq of each num
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print("Reversed string ",rev)

# n=1234
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print("Reversed string ",rev)

#CONTROL STATEMENTS----

#s="hello"

#using break
# for i in s:
#     if(i=="l"):
#         break
#     print(i)

#using continue
# for i in s:
#     if(i=="l"):
#         continue
#     print(i)

#given list
#l=[25,67,34,78,17,44,82]

#print all num
# for i in l:
#     print(i)

#stop loop when i>50
# for i in l:
#     if i>50:
#         break
#     print(i)

#skip all even num
# for i in l:
#     if i%2==0:
#         continue
#     print(i)

#gievn list
#colors=['red','green','yellow','blue','orange','black']

#print all colours
# for i in colors:
#     print(i)

#print col start with b
# for i in colors:
#     if (i[0]=='b'):
#         print(i)

#print first col start with b
# for i in colors:
#      if (i[0]=='b'):
#          print(i)
#          break


#skip col start with b
# for i in colors:
#      if (i[0]=='b'):
#          continue
#      print(i)

# s="python coding is easy and fun"
#print all char upto a specific char(including that char)
# c=input("Enter the character")
# for i in s:
#     print(i)
#     if i==c:
#         break

#write program to check whether number is armstrong
#eg--if n=153 op=1**3+5**3+3**3 =153   1e n=153
#1634 =1**4 +6**4 +3**4 +4**4= (1+1296+81+256) =1634
# n=int(input("Enter number"))
# s=str(n)
# l=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**l
# if (sum==n):
#     print("Armstrong")
# else:
#     print("Not Armstrong")

#factors of a number
#eg 6->1 2 3 6
#8->1 2 4 8
# n=int(input("Enter a number"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)

#for else eg
# for i in range(1,6):
#     print(i)
# else:
#     print("hello")
#
# for i in range(1,6):
#     if i==5:
#         break
#     print(i)
# else:
#     print("hello")

#check whether num is prime or not
#ie has factors as 1 and the num itself
# 1 and -ve numbers are neither prime nor composite

# n=int(input("Enter a number"))
# if (n>1):
#     for i in range(2,n):
#         if n%i==0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime Number")
# else:
#     print("Neither prime nor composite")

#NESTED LOOPING
# l=[10,20,30]
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#print 1 1 1 1
#       2 2 2 2
#       3 3 3 3
# for i in range(1,4):
#     for j in range(1,5):
#         print(i, end =" ")
#     print()

#1 2 3 4
#1 2 3 4
#1 2 3 4
# for i in range(1,4):
#     for j in range(1,5):
#         print(j, end =" ")
#     print()

#* * * *
#* * * *
# * * * *
#* * * *
# for i in range(1,5):
#     for j in range(1,5):
#         print("*", end =" ")
#     print()

#******nested sequencing******
# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)

#given a list
#names=["kelly","alan","jeny"]

#print kelly kelly kelly
#      alan alan alan
#       jeny jeny jeny
# for i in names:
#     for j in range (1,4):
#         print(i,end=" ")
#     print()

#given 2 list
# n=[1,2,3]
# q=['what','when','why']

#print
    #1
    #what when why
    #2
    #what when why
    #3
    #what .....why

# for i in n:
#         print(i)
#         for j in q:
#            print(j,end=" ")
#         print()

#given list
# d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24},{'id':103,'name':'anu','age':25}]
# #print each student detail
# for i in d:
#     #print(i)
#     for j in i.values():
#         print(j)


            # for i in d:   not working check it
            #     print(i)
            #     for k,j in d.items():
            #      print(k,j)

# *
# * *
# * * *
# * * * *

# for i in range (1,5):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()

# *
# * * *
# * * * * *
# * * * * * * *
#
# for i in range (1,8,2):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


#1
#2 2
#3 3 3
#4 4 4 4
#
# for i in range (1,5):
#     for j in range (1,i+1):
#         print(i,end=" ")
#     print()

#1
# 12
# 123
# 1234

# for i in range (1,5):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()

# * * * *
# * * *
#* *
#*

# for i in range (4,0,-1):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()

#given list
#l=[23,45,78,90,12,13,91]

# #print all even num
# for i in l:
#     if i%2==0:
#         print(i)

#print prime num in list
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

#find all prime num in range(1,100)

# for i in range(1,101):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)

#find all armstrong num in range(100,1000)

# for i in range(100,1001):
#     sum=0
#     s=str(i)
#     l=len(s)
#     for j in s:
#         sum=sum+int(j)**l
#     if sum==i:
#         print(i)

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

#1
#2 3
#4 5 6
#7 8 9 10
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k+=1
#     print()



# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#         k+=1
#     print()


# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#     k+=1
#     print()
#
# A
# A B
# A B C
# A B C D
# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#         k+=1
#     print()

# A
# B C D
# E F G H I J
# K L M N O P Q R S T
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         for t in range(1,j+1):
#          print(chr(k),end=' ')
#          k+=1
#     print()
#

# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
# for i in range(1,5):
#     for j in range(1, 5):
#         if i==j:
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()
#

# 1
# 1 0
# 1 0 1
# 1 0 1 0
# for i in range(1,5):
#     for j in range(1, i+1):
#         if j%2==0:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()
#
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

# for i in range(1,6):
#     for j in range(0, i):
#             print(j,end=" ")
#     print()

# s="hello"
# for i in range(len(s)):
#     for j in range(i+1):
#             print(s[j],end=" ")
#     print()

#      *
#     * *
#   * * *
# * * * *
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     k=k-2
#     print()


#this code is same in above but in j loop increase space by one so that op will be pyramid shape
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end="  ")
#     k=k-2
#     print()

#      *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     k=k+2
#     print()

    #      *
    #     *  *
    #   *  *  *
    # *  *  *  *
    #   *  *  *
    #     *  *
    #       *

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end="  ")
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end="  ")
#     k=k+2
#     print()

#       1
#     1  2
#   1  2  3
# 1  2  3  4
#   1  2  3
#     1  2
#       1

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end="  ")
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end="  ")
#     k=k+2
#     print()