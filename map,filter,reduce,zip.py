from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(char):
    return char.capitalize()

print(list(map(capitalize,my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(list(zip(my_strings,my_numbers)))

scores = [73, 20, 65, 19, 76, 100, 88]
def percentage(marks):
    return marks > 50

print(list(filter(percentage,scores)))

def combine(acc,item):
    return acc + item

print(reduce(combine,my_numbers,0))
print(reduce(combine,scores))
print(reduce(combine,(my_numbers + scores)))
