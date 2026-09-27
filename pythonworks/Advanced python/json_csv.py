#               *****JSON FILE****
#   *JSON READ*

# import json
# f=open("data.json","r")
# content=json.load(f)
#
# print(content)
#
# print(content[0])
# print(content[1])
#
# print(content[0]['name'])
# print(content[1]['name'])
#
# print(content[0]['name'],content[0]['age'])
# print(content[1]['name'],content[1]['age'])
#
# f.close()

#   *WRITE*

# import json
# content=[
#     {"title":"Book1","author":"John","price":200},
#     {"title":"Book2","author":"Sam","price":300}
# ]
# f=open('book.json','w')
# json.dump(content,f)
# f.close()

#             ***********CSV FILE**********

### CSV  READ

# import csv
# f=open("data.csv","r")
# content=csv.reader(f)
# for row in content:
#     print(row)
# f.close()

### CSV WRITE
#
# import csv
# f=open("book.csv","w",newline="")
# content=[
#     ['title','author','price'],
#     ['book1','john','ekm'],
#     ['book2','sam','tvm']
# ]