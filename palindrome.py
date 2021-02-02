# # Program to check if a string is palindrome or not
#
# my_str = input("enter the string")
#
# # make it suitable for caseless comparison
# my_str = my_str.casefold()
#
# # reverse the string
# rev_str = reversed(my_str)
# print(rev_str)
# # check if the string is equal to its reverse
# if list(my_str) == list(rev_str):
#    print("The string is a palindrome.")
# else:
#    print("The string is not a palindrome.")
#
# #----------------------------------

# def rev(str):
#     l = len(str)-1
#     char = ''
#     for i in range(len(str)):
#         char = char + str[l]
#         l = l-1
#     return char
#
# mystr = input("enter the string")
# rev_st =rev(mystr)
# if rev_st== mystr:
#     print("it's palindrom")
# else:
#     print("not palindrom")

num = int(input('enter the number'))
length = len(str(num))
new =int(''.join(reversed(str(num))))
print(new)

# string = input("enter the string")
# rev_string = ''.join(reversed(string))
# print(rev_string)
# if string == rev_string:
#     print('its palindrome')
# else:
#     print('not a palindrome')