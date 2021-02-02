def maths(num):
    int(num)
    if num % 5 == 0 and num % 3 == 0:
        print("bizzfizz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("bizz")
    else:
        print(num)


value=input("enter the value ")
maths(int(value))