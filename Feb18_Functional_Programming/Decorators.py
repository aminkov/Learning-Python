def stars_decorator(f):
    print(f("maria"))

    # def wrapper():
    #     print("*" * 50)
    #     f()
    #     print("*" * 50)
    # return wrapper

def greet(user):
    print(f"Howdy {user}!")

@staticmethod
def method():
    pass

# let's decorate greet:
stars_decorator(greet)

#and use it
greet("maria")