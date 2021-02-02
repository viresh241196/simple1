
#def evenlist():

#    return num_list
from largestnoinlist import findmax
num_list = [1,2,3,4,10,5,6,7,8,9]
cmp = findmax(num_list)
count = 0
result = []
for value in num_list:
    if value % 2 == 0 :
        result.append(value)
        count += 1
print(f"Even number in the list are {result}")
print(f"the total count is {count}")
print(f"the max num is {cmp}")