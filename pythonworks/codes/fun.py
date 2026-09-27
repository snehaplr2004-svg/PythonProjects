# #Q.Write Python Programs Using map(), filter(), or reduce()

#sum of +ve even numbers
# a=list(filter(lambda x:x>0 and x%2==0,l))
# import functools
# print(functools.reduce(lambda x, y: x + y, a))
#
#     # #Sum of Positive Odd numbers
# a=list(filter(lambda x:x>0 and x%2!=0,l))
# import functools
# print(functools.reduce(lambda x, y: x + y, a))
#
#     # #Sum of Negative  odd numbers
# a=list(filter(lambda x:x<0 and x%2!=0,l))
# import functools
# print(functools.reduce(lambda x, y: x + y, a))
#
#     # #Sum of Negatve Even numbers
# a=list(filter(lambda x:x<0 and x%2==0,l))
# import functools
# print(functools.reduce(lambda x, y: x + y, a))
#
#     # #Count of Positive numbers
# print(len(list(filter(lambda x: x > 0, l))))
#     # #Count of negative numbers
# print(len(list(filter(lambda x: x < 0, l))))
#
# # 10.Given a list
# nums = ["1", "2", "3", "4"]
# # Convert all Strings to Integers [1,2,3,4]
# print(list(map(lambda x: int(x), nums)))
#
# # 11.
# p= [{'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}]
#
# #print list of product names in Uppercase
# print(list(map(lambda x: x['name'].upper(), p)))
#
# #print products with price greater than 10000
# print(list(filter(lambda x: x['price'] > 10000, p)))
#
# #Find the total price of all products
# import functools
# print(functools.reduce(lambda x, y: x + y['price'], p, 0))
