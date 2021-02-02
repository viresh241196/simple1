# def mul(a,b):
#     return  a*b

f = lambda a, b: a * b
num = int(input("enter the number to display the table"))
for i in range(1, 11):
    print(f"{num} x {i} = {f(num, i)}")
