# D1 = {
#     "name" : "viresh",
#     "age":"23",
#     "birthday":"24 nov 1996"
# }
# D1["home"] = "parel"
# print(D1)
#
# nam = D1['name']
# print(nam)
#----------------------------------------------------------------------------------------------------------------
dirct = {'1':20,'2':50,'3':30,'4':40,'5':20,'7':30,'8':40,'9':20,'10':20}
total = 0
while True:
 select = input()
 if select == 'N':
     break
 else:
    quantity = int(input())
    item = int(dirct[select])
    total = total + item*quantity
print(total)




