# A simplified data for telecom users are stored as two relational tables:
#users data table
#  id |  name   |   number
# ---|---------|---------------
# 1  | "Maria" | "+39587111111"
# 2  | "Ivan"  | "+39587222222"
# 3  | "Asen"  | "+39587333333"
#users bills table
# id |  bill
# ---|---------
# 1  | 25.50
# 2  | 30.48
# 3  |  5.98
# the task:
# Represent the data in appropriate data structures in order to:
# being able to add/remove records from each table
# find and print the name of the user with highest bill
# find and print the name of the user with lowest bill
# The user with highest bill - 30.48 is Ivan
# The user with lowest bill - 5.98 is Asen
users = {
    "1":"Mariya",
    "2":"Ivan",
    "3":"Asen",}
telephones = {
    "1":"+39587111111",
    "2":"+39587222222",
    "3":"+39587333333",}
bills = {
    "1":25.50,
    "2":30.48,
    "3":5.98,}
#calculating the highest bill
highest_bill = 0
id = 0
for i in bills:
    if (bills[i] > highest_bill):
        highest_bill = bills[i]
        id = i
print("The user with highest bill - {} is {}".format(highest_bill, users[id]))
#calculating the lowest bill
lowest_bill=100
id=0
for j in bills:
    if (bills[j] < lowest_bill):
        lowest_bill = bills[j]
        id = j
print("The user with lowest bill - {} is {}".format(lowest_bill, users[id]))