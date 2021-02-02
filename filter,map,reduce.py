from functools import reduce

list_item = [1,2,3,4,5,6,7,8,9,0]


even = list(filter(lambda n: n%2==0 , list_item))
print(even)
map = list(map(lambda a:a*2, even))
print(map)
reduces =reduce(lambda a,b : a+b, even)         #when even want to reduce a list via /*-+ user this tool
print(reduces)