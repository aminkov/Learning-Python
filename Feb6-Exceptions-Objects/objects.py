#everythong in python is an object

class UserAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def withdraw(self, x):
        return self.balance - x

user1 = UserAccount('Mariya', 100)
user2 = UserAccount('Petko', 350)

print(user1.name)
print(user2.balance)
