# def addnums(*args):
#     for i in args:
#         i+=i
#     print(i)

# addnums(1,2,4,56,7,5,4,33,5,6,9)

def foo(**kwargs):
    sum=0
    for i in kwargs.values():
        sum += i
    print(sum)

foo(c=1,b=2,d=3)