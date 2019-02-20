from functools import reduce
l = lambda x,y:x+y
print( l(2,3) )

direction = 'left'

result = lambda direction: direction if direction=='left' else 'right'
print(result(direction))

lst = [3,5,4,3,4,654,34,6,4547,34,634,6]

def even(x):
        if x%2 == 0:
            return True
        else:
            return False

even_numbers = filter(even, lst)
print(list(even_numbers))

list2 = filter(lambda x: True if x%2==0 else False, lst)

print(list(list2))

list3 = map(lambda z,r:z*r, list2, even_numbers)
print(list(list3))

list4 = reduce(lambda x,y: x+y, lst)
print(list4)
