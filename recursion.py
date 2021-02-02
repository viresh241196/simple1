# Python program to find the sum of natural using recursive function


def rec(x):
    if x<=1:
        return x
    else:
        return x + rec(x-1)


num = int(input("enter the number to find the sum"))
result=rec(num)
print(f"the sum of natural {num} is {result}")

