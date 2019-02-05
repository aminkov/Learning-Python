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
new_dict = {}                               #create a new dict to use for sorting
for i,j in distances_from_sofia:            #fill in th enew dict with filtered values
    if (int(j)<1500):
        new_dict[j] = i
ressort = sorted(new_dict)                  #fill in th new dict with filtered values
for i in ressort:                           #use sorted list to solve the task
    print("{} - {}".format(new_dict[i], i)) #cool, it's working!