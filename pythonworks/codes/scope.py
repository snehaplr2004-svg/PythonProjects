#global

# x=20
# print("outside function",x)
# # def f():
# #     print("inside function",x)
#
# f()

# local

# def f():
#     x=8/0
#     print(x)
# f()
# print("out",x)  #not get printed

# #note by using word global
# def f():
#     global x
#     x=80
#     print("Inside f function",x)
# def g():
#     y=30
#     print(x)
#     print("Inside g function",y)
# f()
# g()

#normal/enclosing
def outer():
    x=56
    print("outer",x)
    def inner():
        print("inner",x)
    inner()
outer()
