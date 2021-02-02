def power(n, p):
    if p == 0:
        return 1
    else:
        return n * power(n, p - 1)


num = int(input('enter the number'))
rase_to = int(input('enter the power'))
ans = power(num, rase_to)
print(f'the result is {ans}')
