# 1.file read
# 2.file write
# 3.file append
# 4.file search
# 5.file delete
# 6.exit
def file_read():
    filename = input("Enter file name:")
    f = open(filename, "r")
    s = f.read()
    print(s)
    f.close()

def file_write():
    filename = input("Enter file name:")
    f = open(filename, "w")
    wr=input("Enter file content to be written:")
    f.write(wr)
    f.close()

def file_append():
    filename = input("Enter file name:")
    f = open(filename, "a")
    ap = input("Enter file content to append:")
    f.write(ap)
    f.close()

def file_search():
    filename = input("Enter file name:")
    f = open(filename, "r")
    s = f.read()
    wr = input("Enter file content to be searched:")
    if wr in s:
     print(wr,"is found ")
    else:
     print("not found")
    f.close()

def file_delete():
    filename = input("Enter file name to be deleted:")
    import os
    os.remove(filename)

while(1):           #while(True) also correct
    print("menu driven file operation")
    print("1.file read")
    print("2.file write")
    print("3.file append")
    print("4.file search")
    print("5.file delete")
    print("6.exit")

    ch=int(input("Enter your choice:"))
    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    else:
        exit()