#variables into a finction are local to that function

x = 2

def foo(x):
    print(x)

foo(4)
print(x)

print('working with global variables in functions')
def foo2():
    global x
    print(x)

foo2()
print(x)
