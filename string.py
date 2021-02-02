lines = []
for T in range(int(input())):
    lines.append(input())
for line in lines:
    string = line.split(' ')
    loc = []
    for i in range(len(string)-1):
        if string[i].lower() == string[i+1].lower():
            loc.append(i+1)

    loc = list(reversed(loc))
    for item in range(len(loc)):
        string.pop(loc[item])


    for cha in string:
        print(cha+' ', end='')
    print('')
