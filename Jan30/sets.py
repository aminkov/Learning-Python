#SETs
prices_set = {1.20, 3.450, 8.47, 23.67, 1.20}

print(prices_set)

#SETs can be used to remove duplicate values from a list
numbers_list = [1,1,1,2,3,4,5,6,7,7,5,4,3,2,1,23,34,545,3,3,2,2,3,4,5,4,43,2]
numbers_set = set(numbers_list)
print(numbers_set)

a = {1,2,3}
b = {3,4,5,6}
#returning a set of the united sets 
unionset = a | b
print(unionset)

b.union(unionset)
print(b)