def list1():
    yield 5
    yield 7
    yield 8
    yield 9


def topten():
    n = 1
    while n <= 10:
        sqr = n*n
        yield sqr
        n += 1


obj = list1()

for i in obj:
    print(i)



