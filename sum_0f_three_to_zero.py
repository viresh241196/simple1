# def div(arr, n):
#     found = False
#     for i in range(0, n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 if arr[i]+arr[j]+arr[k] == 0:
#                     print(arr[i], arr[j], arr[k])
#                     found = True
#     if found == False:
#         print('does not exit')


# arr = [-1, -1, -2, -3]
# n = len(arr)
# div(arr, n)

n=4
for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                print('hi')