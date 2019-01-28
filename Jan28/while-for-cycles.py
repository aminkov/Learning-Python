#print the numbers from 1 to 10 but stop untill 5 is reached
arr = [1,2,3,4,5,6,7,8,9]
for el in arr:
    print(el)
    if el == 5:
        break


#ask the user to enter a positive number


while True:
    usernumber = int(input("Enter a number: "))
    if usernumber >= 0:
        break
print(usernumber)