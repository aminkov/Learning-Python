#define a function with a parameter 'x' with default value of 5.
def foo(x=5):
    #what you write into the belows comment, goes to the help of the function:
    '''This function gets a string for input and returns it'''
    #function what to do
    print(x)
#call the function
#if we pass an explicit value to the function - it replaces the default value
foo(3)

def sum_num(x,y):
    print(x+y)

sum_num(3,4)

def checkin(name, surname, age, address):
    print(name)
    print(surname)
    print(age)
    print(address)

checkin('Ivan', 'Ivanov', 23, 'Sofia str 1')
