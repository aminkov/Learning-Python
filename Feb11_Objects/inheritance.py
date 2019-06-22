class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Developer(Person):
    def __init__(self, name, age, skills):
        super().__init__(name, age)
        self.skills = skills

class Manager(Person):
    def __init__(self, name, age, manage):
        super().__init__(name, age)
        self.manage = manage
        
    def __str__ (self):
        for i in range(len(self.manage)):
            return "Manager: {}, Employee: {}".format(self.name, self.manage[i].name)
    def listproperties(self):
            print("I am a manager and my name is {} and my age is {}".format(self.name, self.age))
            print("My employees are:")
            for m in range(len(self.manage)):
                print(self.manage[m].name)
            print("My employees' skills are:")
            for l in range(len(self.manage)):
                print("-"*6)
                print(self.manage[l].name)
                print("-"*6)
                for n in self.manage[l].skills:
                    print(n)
                print("-"*6)
                print("*"*20)

dev1 = Developer('Pesho',23, ['Python', 'Java', 'Rubi'])
dev2 = Developer('Mitko',45, ['C++', 'HTML', 'CSS'])
dev3 = Developer('Marto',5, ['C', 'Kotlin', 'Javascript'])
dev4 = Developer('Pesho',23, ['Python', 'Java', 'Rubi'])
dev5 = Developer('Mitko',45, ['C++', 'HTML', 'CSS'])
dev6 = Developer('Marto',5, ['C', 'Kotlin', 'Javascript'])

manager1  = Manager('George', 40, [dev1, dev2, dev3, dev4, dev5, dev6])

manager1.listproperties()




