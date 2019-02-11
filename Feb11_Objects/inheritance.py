class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Developer(Person):
    def __init__(self, name, age, skills):
        self.skills = skills

class Manager(Person):
    def __init__(self, name, age, manage):
        self.manage = manage
        
    def __str__ (self):
        for i in range(len(self.manage)):
            return "Manager: {}, Employee: {}".format(self.name, self.manage[i].name)

dev1 = Developer('Pesho',23, ['Python', 'Java', 'Rubi'])
dev2 = Developer('Mitko',45, ['C++', 'HTML', 'CSS'])

manager1  = Manager('George', 40, [dev1,dev2])

print(manager1)
