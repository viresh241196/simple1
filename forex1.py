print("""enter the shopping items from the list
burger
cake
pizza """)
b = ""
c = ""
p = ""
x = ''
while x != "quit":
    x = input("enter the item or quit")
    if x == "quit":
        break
    y = input("enter the quantity")
    if x == "burger":
        b = int(10 * y)
        print(b)
    elif x == "cake":
        c = int(20 * y)
        print(c)
    elif x == "pizza":
        p = int(30 * y)
        print(p)
    else:
        print("Bad Input")
Total = 0
Total = int(b) + int(c) + int(p)
print(f"the total amount is {Total}")

