a= 15
b = 0
try:
    print("resources opened")
    c= a/b
    print(c)
    num = int(input("enter a number"))
except ZeroDivisionError as e:
    print("you cant divide by 0", e)
except ValueError as e:
    print("invalid input")
except Exception:
    print("something went wrong")
finally:
    print("resources closed")



