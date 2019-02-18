from functools import(reduce)
#filtering zeroes with lambda
l1 = [1,2,3,4,0,56,7,8]

l2 = reduce(lambda x,y: y!=0 and x/y, l1)

print(l2)

#filtering zeros with filter
l1 = [1,2,3,4,0,56,7,8]

l2 = reduce(lambda x,y: x/y, filter(lambda z: z, l1))

print(l2)