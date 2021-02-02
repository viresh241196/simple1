my_dict = {num: num ** 2 for num in [1, 2, 3]}
print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = {value for value in some_list if some_list.count(value) > 1}
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
