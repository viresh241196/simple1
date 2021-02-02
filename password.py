username = input('Enter your name')
password = input('Enter your password')
passlen = len(password)
count = '*' * passlen
print(f"Hi {username}, your password {count} is {passlen} letter long.")