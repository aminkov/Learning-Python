class Duck:
    def quack(self):
        print('Quack, Quack')

class Goose:
    def quack(self):
        print('Quack!')

def quack(obj):
    obj.quack()


donald = Duck()
lea = Goose()