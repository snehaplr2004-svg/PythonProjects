#write operation
# f=open('k.txt','w')

#syntax

# f.write('string')
# f.writelines(list)

# f.write("hello\n")
# f.write("python\n")

# f.writelines(['hello\n','python\n'])
# f.close()

#read operation
#
# f=open('k.txt',"r")
# s=f.read()
# print(s)
# print(type(s))

#or method


# f=open('k.txt',"r")
# s=f.readlines()
# print(s)
# print(type(s))

#write prgram to read txt file and display no of lines in a file

# f=open('k.txt',"r")
# s=f.readlines()
# print(len(s))
#f.close

# f=open('k.txt',"r")
# s=f.read()
# print(s.split())
# print(len(s.split()))
# f.close()

#update second line to a file

# f=open('k.txt',"r")
# s=f.readlines()
# s[1]= "new line\n"
# f.close()
#
# f=open('k.txt',"w")
# a=f.writelines(s)
# f.close()

#display last 5 lines in file
#
# f=open("k.txt","r")
# s=f.readlines()
# print(s[-5: ])
# f.close()

#search particular word
#
# w=input("enter word")
# f=open("k.txt","r")
# s=f.read()
# if w in s:
#     print("Found")
# else:
#     print("Not Found")
# f.close()

#find no of letter,digit,and spaces in a file
#
# l=0
# d=0
# sp=0
# f=open('k.txt','r')
# s=f.read()
# for i in s:
#     if i.isdigit():
#         d+=1
#     elif i.isalpha():
#         l+=1
#     elif i.isspace():
#         sp+=1
#     else:
#         pass
# print("letter count=",l,"Digit count =",d,"Space count =",sp)
# f.close()

#reverse line in file

# f = open("k.txt", "r")
# s = f.readlines()
# s=s[::-1]
# f.close()
# f=open("k.txt","w")
# s=f.writelines(s)
# f.close()

#a file total_students.txt contain names of all students in class
# and file passed_students.txt contain names of students who passed.txt in exam
#read names from both file
#find names who didnot pass
#write their name to a new file named failed_students.txt.txt ,one name per line

# f=open("total_students.txt","w")
# f.write(" anu \n kevin\n neeraj\n ammu\n kiran ")
# f.close()

# f=open("total_students.txt","r")
# s=f.readlines()
# print(s)
# g=open("passed.txt","r")
# a=g.readlines()
# print(a)
# h=open("failed_students.txt","w")
# for i in s:
#     if i not in a:
#         h.write(i)
# f.close()
# g.close()
# h.close()

##APPEND

# f=open('k.txt','a')
# f.write("hybrid")
# f.close()

#write a program to append contents from one file into another txt file

# f=open("k.txt","r")
# s=f.read()
# h=open("failed_students.txt","a")
# h.write(s)
# f.close()
# h.close()

# f=open("k.txt","a+")
# f.write("python")
# s=f.read()
# print(s)    #in this case printing not occur bz the pointer is in the end which is blank
# f.close()

#for changing position the function used are seek(),tell()
#
# f=open("k.txt","a+")
#
# print("First position",f.tell())
# f.write("python")
#
# print("second position ",f.tell())
# f.seek(0)
#
# print("third position ",f.tell())
# s=f.read()
#
# print(s)
# f.close()

#DELETE
#
# import os
# os.remove('failed_student.txt')
# print("file removes")