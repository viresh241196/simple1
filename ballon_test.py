T = int(input())
g,p = map(int, input().split())
for n in range(T):
    participant = int(input())
    total =  0
    cost = []
    for event in range(participant):
        value1,value2 = map(int, input().split())
        total += value1*g + value2*p
    cost.append(total)
    for item in cost:
        print(item)

