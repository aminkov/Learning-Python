#we use if/elif/else if we need to use switch in python. We don't have switch-case in python.
#example
task1 = 1
task2 = 0
#end of task switchers

if task1 == 1:
    while True:
        userchoice = int(input("Please enter a number"))
        if userchoice == 1:
            print("you entered 1 ")
        elif userchoice == 2:
            print("you entered 2 ")
        elif userchoice == 3:
            print("you entered 3 ")
        else:
            print(userchoice)
            break

#Task 2
#Prompt the user to enter a pass untill the pass is 3 or more symbols
if task2 == 1:
    while True:
        userpass = input("Please, enter pass: ")
        if len(userpass) >=3:
            break



