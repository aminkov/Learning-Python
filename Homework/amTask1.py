#Given are two lists of names:
#first_names with items "ivan", "maria", "petar"
#sur_names with items "ivanov", "popova", "petrov"
#Write a program which will make a third list: names, which will holds the items from the two l[task_1.py][task_1.py]ist above as given:
# print(names)
## ['ivan', 'maria', 'petar', 'ivanov', 'popova', 'petrov']

names = ("ivan", "maria", "petar")
surnames = ("ivanov", "popova", "petrov")
all_names = names + surnames
print(all_names)