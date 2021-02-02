message = input(">")
statement = message.split(' ')
book ={
    "mc":"bc",
    "fuck":"fuck you"
}
output = ""
for word in statement:
    output += book.get(word,word) + " "
print(output)