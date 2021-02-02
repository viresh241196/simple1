import random
ar=[]
for i in range(10):
    num = random.randint(1,100)
    ar.append(num)
max_n=max(ar[0],ar[1])
sec_max=min(ar[0],ar[1])
for x in ar:
    if x > max_n:
        sec_max=max_n
        max_n=x
print(ar)
print(max_n)
print(sec_max)