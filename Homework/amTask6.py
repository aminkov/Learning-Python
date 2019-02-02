""" Task 6 [task_6.py]
Given are next list of distances from Sofia:
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
Write a program, which will outputs only the distances from Sofia which are bellow 1500km
Distances bellow 1500km from Sofia are:
Bansko - 97
Alexandria - 1403
Nice - 1307
Szeged - 469
Palermo - 987 """

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
for i,j in distances_from_sofia:
    if (int(j)<1500):
        print("{} - {}".format(i,j))
    a += 1
