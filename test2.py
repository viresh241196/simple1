s = 'django'
print(s[0], s[-1], s[0:4], s[1:4], s[4:6])
print(s[::-1])

l = [3, 7, [1, 4, 'hello']]
l[2][2] = 'goodbye'
print(l)

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])
d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {'k1': [{'nested_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nested_key'][1][0])

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]
newtuple = set(mylist)
print(newtuple)
