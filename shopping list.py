import sqlite3


def cake(quantity):
    total = int(quantity) * 20
    return total


def pizza(quantity):
    total = int(quantity) * 50
    return total


def burger(quantity):
    total = int(quantity) * 30
    return total


def insert_db(name , mobile, bill):
    with conn:
        content = {'name':name, 'mobile':mobile, 'bill': bill}
        c.execute("INSERT INTO shopping2 VALUES (:name ,:mobile ,:bill )",
                  content)


conn = sqlite3.connect('shopping2.db')
c = conn.cursor()

#c.execute("""CREATE TABLE shopping2 (
#            Srno INTEGER PRIMARY KEY AUTOINCREMENT,
#            name text,
#            mobile integer,
#           bill integer
#            )""")


print("""enter the shopping items from the list
burger  30
cake    20
pizza   50 """)
item = ""
result = result1 = result2 = result3 = burger_count = pizza_count = cake_count = 0
while item != "quit":
    item = input("enter the item or quit")
    if item == "quit":
        break
    else:
        qunty = input("enter the quantity")
        if item == "cake":
            cake_count = qunty
            result1 = cake(qunty) #+ result1
        elif item == "pizza":
            pizza_count = qunty
            result2 = pizza(qunty) #+ result2
        elif item == "burger":
            burger_count = qunty
            result3 = burger(qunty) #+ result3
        else:
            print("BAD Input")
result = result1 + result2 + result3
name = input('enter your name ')
mobile = input('enter your mobile number ')
insert_db(name, mobile, result)
conn.close()
print(f"""The Total Bill is as follow
            item        count        amount
            cake        {cake_count}        {result1}
            burger      {burger_count}      {result2}
            pizza       {pizza_count}       {result3}
            _________________________________________
            Total               {result}""")




