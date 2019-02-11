class BankAccount():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def deposit(self, sum):
        self.amount = self.amount + sum

    def withdraw(self, sum):
        self.amount = self.amount - sum
    
    def __str__(self):
        return "{}'s balance is: {}".format(self.name, self.amount)

maria_account = BankAccount("Maria", 1_300)
pesho_account = BankAccount("Pesho", 400)
maria_account.deposit(250)
pesho_account.withdraw(100)

print("Maria's balance is: {}".format(maria_account.amount))
print("Pesho's balance is: {}".format(pesho_account.amount))
print(maria_account)
