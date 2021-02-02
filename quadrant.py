a = []
n = int(input('length'))
for i in range(n):
    x = float(input())
    a.append(x)
r =list(reversed(a))
result = r[0]*r[1]*r[2]*r[3]
print(result)
