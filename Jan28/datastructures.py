#Lists
#Tuples
#Ranges
#THere are no arrays in Python!!!

#task switches
task1 = 0  #lists
task2 = 0  #mathrixes
task3 = 0  # tuples
task4 = 0  # ranges
task5 = 0  # exercises
task6 = 0  #slicing
task7 = 1  #task


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


if task5 == 1:
    l1 = [1,2,3]
    l2 = [4,5,6]

    print(l1 + l2)
    print(l1 * 5)

    print(3 in range(4))  #returns "True" because 3 is in 1-4
    username = "blahblah"
    print( "h" not in username ) #trturns "False" because "h" is in "blahblah"

if task6 == 1:
    #slicing
    #str = list[start:end:step]
    l1 = [1,2,3]
    l2 = [4,5,6]
    l = l1 + l2

    print(l[2:])
    print(l[:2])

    str = "abcdefg"
    print(str[::2])

if task7 == 1:
    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
    sm = m[0][1]
    print(sm)