#Given are two lists first_names and sur_names as in previous task.
#From first_names and sur_names create a third list:
#names which will hold the items from the two list with next order:
# print(names)
# ['ivan', 'ivanov', 'maria', 'popova', 'petar', 'petrov']

names = ["ivan", "maria", "petar"]
surnames = ["ivanov", "popova", "petrov"]
names.insert(1, surnames[0])
names.insert(3, surnames[1])
names.insert(5, surnames[2])
print(names)

