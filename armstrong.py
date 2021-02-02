# numo = int(input("enter the number"))
# sum = 0
# num = numo
# while num > 0:
#      digit = num % 10
#      sum = sum+digit**3
#      num = num // 10
# if sum == numo:
#      print("the number is armstrong number")
#  else:
#      print("the number is not armstrong number")


# ----------------------------------------------------------------------
# start = int(input("enter the starting point"))
# end = int(input("enter the ending point"))
# list = []
#
# for i in range(start,end+1):
#     num = i
#     numlen= len(str(num))
#     sum = 0
#     while num >0:
#         digit = num % 10
#         sum = sum + digit**numlen
#         num = num // 10
#     if sum == i:
#         list.append(i)
# if list != []:
#     print(f"following are the armstrong number {list}")
# else:
#     print("no number ")


def armstrongNumber(arr):
    ans = []
    for num in arr:
        temp = num
        Sum = 0
        while temp > 0:
            digit = temp % 10
            Sum = Sum + digit ** len(str(num))
            temp = temp // 10
        if Sum == num:
            ans.append('the number is armstrong')
        else:
            ans.append('the number is not armstrong')
    return ans


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = []
    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)
    print(arr)
    result = armstrongNumber(arr)
    print('\n'.join(result))
