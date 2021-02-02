list = [1 , 3, 4, 5, 7, 5,8 ,4, 3, 3,4,6,7,4]
print(list)
newlist = []

for r in list:
    if r not in newlist:
        newlist.append(r)
print(newlist)