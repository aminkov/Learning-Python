""" Write a program which will ask the user to enter N names. N is also entered by the user, after respective prompt.
The names entered by the user, should be stored in a list names and will be printed to output.
Here is how your program should behave:
 How many names are you going to enter? 3
Enter a name, please: Maria
Enter a name, please: Ivan
Enter a name, please: Stoyan
******************************
The names you've entered are:
Maria
Ivan
Stoyan """

n = int(input("How many names are you going to enter? "))
print(n)
a = 0
name = []
for i in range(n):
    name.insert(a, input("Enter a name, please: "))
    a += 1
print("******************************")
print("The names you've entered are: ")
for i in name:
    print(i)
