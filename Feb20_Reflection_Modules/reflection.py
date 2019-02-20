# dir() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
maria = Person("Maria Popova", 25)
print(dir(maria))

a = 5
print(dir(a))
lis=[1,2,3]
print(dir(lis))

#type(function)

print(type(a))
print(type(lis))
print(type(maria))


print(id(a))
print(id(5))
print(id(lis))
print(id(maria))

