num = [3,5,6,8,9]

it = iter(num)
print(it.__next__())

print(next(it))

for i in num:
    print(i)

