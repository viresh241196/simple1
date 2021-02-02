# num = int(input(("enter the last number")))
# a= 0
# b= 1
# print("the sequence is")
# print(a)
# print(b)
# for i in range(num-2):
#     f = lambda a,b: a+b     #c=a+b
#     c = f(a,b)
#     print(c)
#     a= b
#     b = c
#

def sum(a,b):
    return a+b


last = 10
a = 0
b = 1
for i in range(last-2):
    c = sum(a,b)
    print(c)
    a = b
    b = c