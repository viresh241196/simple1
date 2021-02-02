#wap inpu T no. of task
#a and b are the numbers
#output = (a^b) %100000007
t = int(input())
result = []
for task in range(t):
    num1 = int(input())
    num2 = int(input())
    c = num1 ** num2
    result.append(c%1000000007)
for op in result:
    print(op)

