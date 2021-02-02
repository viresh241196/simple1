# lists = []
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             # prime = False
#             break
#     else:
#         # prime = True
#         lists.append(i)
# print(lists)
# ---------------------------------------------------------------------------------------
# ##wap prime no
# lists = []
# for num in range(2, 10000):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         lists.append(num)
#     if len(lists) < 100:       #here we keep count of intem inside list
#         continue
#     else:
#         break                    #break once 100
# print(lists)
# print(len(lists))
# ---------------------------------------------------------------------------------------
# ##wap armstrong
# num = int(input('enter the number'))
# lengths = len(str(num))
# summ = 0
# ref = num
# while num != 0:
#     digit = num % 10
#     summ = int(summ) + int(digit**lengths)
#     num = num // 10
# if summ == ref:
#     print('its a armstrong number')
# else:
#     print("it's not a armstrong number")
# ---------------------------------------------------------------------------------------
# ##wap palindrome
# num = int(input('enter the number'))
# length = len(str(num))
# new =int(''.join(reversed(str(num))))
# print(new)
#
# ---------------------------------------------------------------------------------------
# ##wap palindrome num
# num = int(input('enter the number'))
# rev =int(''.join(reversed(str(num))))
# print(rev)
# if num == rev:
#     print('number is palindrome')
# else:
#     print('number is not palindrome')
# ---------------------------------------------------------------------------------------
# num = []
# ad = []
# for i in range(1, 21):
#     num.append(i)
# print(num)
# for j in num:
#     if j % 2 == 0:
#         ad.append(j)
# print(ad)
# ---------------------------------------------------------------------------------------
# ##wap to find odd num from range
# num = []
# odd = []
# for i in range(1, 21):
#     num.append(i)
# for j in num:
#     if j % 2 != 0:
#         odd.append(j)
# print(odd)
# ---------------------------------------------------------------------------------------
# ##wap fibonacci series of 100 num
# b=a=1
# print(a)
# print(b)
# for i in range(3,20):
#     c= a+b
#     if c > 100:
#         break
#     print(c)
#     a = b
#     b = c
# ---------------------------------------------------------------------------------------
# ##wap to print pattern
# num=1
# for i in range(0,6):
#     for j in range(0,i):
#         print(f' {num}',end='')
#         num = num + 1
#     print('\r')
# --------------------------------------------------------------------------------------
# ##wap to find the sum of factorial of given range
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# sum = 0
# lists = []
# last = int(input('enter the alst number'))
# for i in range(1, last + 1):
#     sum = sum + fact(i)
#     lists.append(sum)
# print(lists)
# print(sum)
#
# ---------------------------------------------------------------------------------------
# ##wap to find sum of odd no in given range
# def oddeven(n):
#     if n%2==0:
#         return 0
#     else:
#         return 1
#
# last = int(input('enter the last number'))
# sum =0
# for i in range(1,last+1):
#     value = oddeven(i)
#     if value == 1:
#         sum += i
# print(sum)
#
# ---------------------------------------------------------------------------------------
# ##wap to find fibonacci series of n th term
# last = int(input('enter the last number'))
# a = 1
# b = 1
# print(a)
# print(b)
# for i in range(2, last):
#     c = a + b
#     print(c)
#     a = b
#     b = c
# ---------------------------------------------------------------------------------------
# ##wap sum of all prime num
# last = int(input("enter the last number"))
# sum = 0
# for num in range(2,last+1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         sum += num
# print(sum)
# -----------------------------------------------------------------------------------------
#
# num = 1
# for i in range(5, 0, -1):
#     for j in range(0, i):
#         # ch = chr(num)
#         print(f' {num}', end=' ')
#         num = num + 1
#     print('\r')
# -------------------------------------------------------------------------------------------
# N = 10
# cust = int(input())
# if cust > 5 or cust == 0:
#     print('invalid output')
# else:
#     remaining = N - cust
#     print(f'number of candies sold : {cust}\n number of candies available:{remaining} ')
# ------------------------------------------------------------------------------------------
# ##wap bubble sort
num = [5, 7, 2, 5, 6, 8]
max = num[0]
new= []
for j in range(0,5):
    for i in range(0,5):
        a = num[i]
        b = num[i+1]
        if a<b:
            num[i] = b
            num[i+1] = a
print(num)
# ------------------------------------------------------------------------------------------
# ##wap to find the union of list
# num =[1,2,3,4,5]
# num2 = [6,7,8,9]
# for i in range(0,4):
#     num.append(num2[i])
# print(num)
# ------------------------------------------------------------------------------------------
# ##wap to find the intersection of list
# num =[1,2,3,4,5]
# num2 = [5,2,7,3,8,9]
# inter = []
# for i in num:
#     if i in num2:
#         inter.append(i)
# print(inter)
#
