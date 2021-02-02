# t = int(input())
# result = []
# for case in range(t):
#     event = int(input())
#     matrix = []
#     for row in range(1, event + 1):
#         col = []
#         for column in range(1, event + 1):
#             col.append(row + column)
#         matrix.append(col)
#     sum = 0
#     for i in matrix:
#         for j in i:
#             sum = sum + j
#     result.append(sum)
# for op in result:
#     print(op)

P = 12
while P > 0:
    P -= 1
    try:
        a, b = map(int, input().split(' '))
        print(a + b)
    except:
        continue
