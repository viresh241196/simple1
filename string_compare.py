for T in range(int(input())):
    string1 = list(input())
    string2 = list(input())
    count =[]
    for x in string1:
        if x in string2:
            count.append(x)
    total = 2*len(count)
    print(total)