v=input(print("phone : "))
dic = {
    '1' : "one",
    "2" : 'two',
    "3" : "three",
    "4" : "four",
    "5": "five "
}
output=""
for char in v:
    output+=dic.get(char, "!") + " "
print(output)



