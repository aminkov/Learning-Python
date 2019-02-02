""" Task 6 - advanced
Using the sorted() function explained in Sorting HOW TO, output the sorted lists of filtered distances in ascending order:
Bansko - 97
Szeged - 469
Palermo - 987
Nice - 1307
Alexandria - 1403 """

distances_from_sofia = [
    ("Bansko", 97),
    ("Brussels", 1701),
    ("Alexandria", 1403),
    ("Nice", 1307),
    ("Szeged", 469),
    ("Dublin", 2479),
    ("Palermo", 987),
    ("Moscow", 1779),
    ("Oslo", 2098),
    ("London", 2019),
    ("Madrid", 2259),
]
a=0
#create a new dict to use for sorting
new_dict = {}  
#fill in th enew dict with filtered values
for i,j in distances_from_sofia:
    if (int(j)<1500):
        new_dict[j] = i
    a += 1
#sort keys of new dict in a list
ressort = sorted(new_dict)
#use sorted list to solve the task
for i in ressort:
    print("{} - {}".format(new_dict[i], i))
#cool, it's working!