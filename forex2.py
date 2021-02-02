num = [5, 2, 5, 2, 2]

for z in num:
    print("x" * z)

for c1 in num:
    ot = ''
    for c2 in range(c1):
         ot = ot + 'x'
    print(ot)