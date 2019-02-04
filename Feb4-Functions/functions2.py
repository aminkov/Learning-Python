def addnums(*args):
    for i in args:
        i+=i
    print(i)

l = [1,2,4,56,7,5,4,33,5,6,9]
addnums(*l)