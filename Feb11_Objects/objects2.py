class A:
    count = 0
    @classmethod
    def counter(cls):
        cls.count +=1

    def __init__(self):
         A.count += 1
         self.count += 1

a1 = A()
a2 = A()
a3 = A()

print(A.count)