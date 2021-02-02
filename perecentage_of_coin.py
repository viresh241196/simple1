import random
head=0
tail=0
for i in range(10):
    num=random.randint(0, 1)
    if num==0:
        head+=1
    else:
        tail+=1
if head > tail:
    per=(head/10)*100
    print(f"head won and it's percentage is {per}")
else:
    per=(tail/10)*100
    print(f"tail won and it's percentage is {per}")
