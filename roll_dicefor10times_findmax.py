import random
record={}
min=100
max=0
for i in range(1,7):
    record[i]=0

while True:
    dice=random.randint(1,6)
    record[dice]+=1
    if min > record[dice]:
        min_key=dice
        min=record[dice]
    if record[dice] >=10:
        max=record[dice]
        max_key=dice
        break  
print(max_key,max,min_key,min)
