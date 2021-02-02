a = []
count = int(input('enter the no of count'))
for i in range(count):
    num = float(input('enter the number'))
    a.append(num)
if len(a) > 3 and len(a) < 100000:
    lt = []
    product = 0
    for i in range(0, count - 3):
        sum = a[i] * a[i + 1] * a[i + 2] * a[i + 3]
        lt.append(sum)
        if sum > product:
            product = sum
    print(lt)
    print(product)
else:
    print('invalid input')

# a =[-3,1,2,-2,5,6,1]
# for i in range(0,3):
#     sum = a[i]*a[i+1]*a[i+2]*a[i+3]
#     print(sum)
