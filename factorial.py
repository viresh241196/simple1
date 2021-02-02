# def fact(n):
#     a = 1
#     for i in range(1, n+1):
#         a = i * a
#     return a
#
#
def factorial(n):
    if n== 0:
        return 1
    return n * factorial(n-1)


output = factorial(2)
print(output)

# def power(n, p):
#     # if p!=0:
#     #     return n * power(n,p-1)
#     # else:
#     #     return 1
#     if p == 0:
#         return 1
#     else:
#         return n * power(n,p-1)
#
#
# num = int(input('enter the number'))
# raseto = int(input('enter the power'))
# ans = power(num, raseto)
# print(ans)
