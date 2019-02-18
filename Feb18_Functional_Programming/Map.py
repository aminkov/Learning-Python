# map(function, iterable, ...)

l = [1,2,3,4,56,7,8]
l2 = map(lambda x: x**2, l)
print(list(l2))

l1 = [1,2,3,4,56,7,8]
l2 = [3,4,5,3,6,2,9]

l3 = map(lambda x,y: x+y, l1, l2)
print(list(l3))
