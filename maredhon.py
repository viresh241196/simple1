entry_list = []
while True:
    entry = input('enter the distance covered or q to quit')
    if entry != 'q':
        entry_list.append(entry)
    else:
        break
new_list = []
for item in entry_list:
    if item != '40':
        new_list.append(item)
    else:
        pass
new_list = sorted(new_list)
new_list = list(reversed(new_list))
print(f'the top three runner are {new_list[0]},{new_list[1]},{new_list[2]}')

