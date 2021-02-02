import sys
import random

start = int(sys.argv[1])
end = int(sys.argv[2])

choice = int(input(f'Enter a number from {start} to {end}  \b'))
num = int(random.randint(int(start), int(end)))
print(num)
while num != choice:
    if choice < start or choice > end:
        print('please enter a value within range')
    choice = input('try again')
    if int(choice) == num:
        break
    else:
        continue
print("Congratulation you win")
