class Person:
    count = 1
    nationality = 'bg'
    def __init__(self, name, age):
        Person.count +=1
        self.name = name
        self.age = age
    def say_hello(self):
        print("I am {}, my age is {}".format(self.name, self.age))

maria = Person("Maria", 100)
pesho = Person("Pesho", 50)
maria.age = 80

print(maria.name, maria.age)
print(Person.count)

print(Person.say_hello(maria))
print(maria.say_hello())



