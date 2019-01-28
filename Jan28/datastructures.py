#Lists
#Tuples
#Ranges
#THere are no arrays in Python!!!

#task switches
task1 = 0  #lists
task2 = 0  #mathrixes
task3 = 0  # tuples
task4 = 1  # ranges


if task1 == 1:
    fruits = [5]
    print(fruits)
    fruits[0] = "apple"
    print(fruits[0])

#print all elements in a matrix
if task2 == 1:
    matrix = [
        [1,2,3],
        [4,44,6],
        [7,33,9],
    ]

    print(matrix)

    for i in matrix:
        print(i)
        for j in i:
            print(j)
#end of matrixes
#ranges
# range (start,stop,step)
if task4 == 1:
    r1 = range(2,11,2)
    print(list(r1))

    for i in range(2,11,2):
        print(i)

#printing all odd numbers in [-10..0]
    for m in range(-9,1,2):
        print(m)



