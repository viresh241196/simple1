num = int(input('enter the number'))
flag= 0
for i in range(2, num):
    if (num % i)== 0:
        flag =1
        #prime = False
        break
#else:
#   prime = True

if flag == 0:
    print(f" {num} is prime")
else:
    print(f" {num} is not prime")
# if prime is True:
#     print(f" {num} is prime")
# else:
#     print(f" {num} is not prime")

#
# #_________________________________________________________________________
# prime_list = []
# last_num = int(input('enter the last number'))
# for z in range(2, last_num):
#     for j in range(2,z):
#         if (z % j) == 0:
#             break
#     else:
#         prime_list.append(z)
#
# print(prime_list)
#------------------------------------------------------------------------------------
# lower = 2
# upper = 20
#
# print("Prime numbers between", lower, "and", upper, "are:")
#
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)


# num =int(input('num'))
# a=[]
# for i in range(1,num+1):
#     if num%i == 0:
#         flag=0
#         for j in range(2, int(i/2)):
#             if (i % j)== 0:
#                 flag =1
#                 #prime = False
#                 break
#         if flag == 0:
#             a.append(i)
# print(a)
            