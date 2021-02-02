
def mult(a,b):
    (result) = int(a) * int(b)
    return result


def div(a,b):
    (result) = int(a) // int(b)
    return result


def add(a,b):
    result = int(a) + int(b)
    return result


def sub(a,b):
    result = int(a) - int(b)
    return result


print('!!Calculator!!')
a = input('enter first number')
b = input('enter second number')
choice = input("""what you want to do
        1.addition
        2.subtraction
        3.division
        4.multiplication""")
if choice == '1':
    result = add(a,b)
elif choice == '2':
    result = sub(a, b)
elif choice == '3':
    result = div(a, b)
elif choice == '4':
    result = mult(a, b)
else:
    print('bad input')

print(f'the result is {result}')