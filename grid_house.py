# grid = int(input())
# village = input()
# con = village.find('.')
# new = ''
# if con!=-1:
#     for event in village:
#         if event =='.':
#             new += 'B'
#         else:
#             new += event
#     print('YES')
#     print(new)          
# else:
#     print('NO')

grid = int(input())

if 1<=grid<=20:
    village = input()
    if 'HH' in village:
        print("NO")
    else:
        print(village.replace('.',"B"))