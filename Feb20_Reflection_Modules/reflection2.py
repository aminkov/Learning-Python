class Person():
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def greet(self):
        print(f"Hello {self.name}")

class Employee(Person):
    def __init__(self, name, age, cv):
        super().__init__(name, age)
        self.cv = cv

pesho = Employee("Pesho", 32, "CV")

print(pesho)

if issubclass(type(pesho), Person):
    print("Pesho is a subclass of Person")