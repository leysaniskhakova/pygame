from animal import *

class A(object):
  """docstring for A"""
  def __init__(self, arg):
    super(A, self).__init__()
    self.arg = arg


    

class B(A):
  pass



a = A("ы")
b = B("ыы")

print("###")
print(a.arg)
print("---")
print(b.arg)
print("###")


class Dog():
  def __init__(self, name):
    self.name = name

  def say(self):
    return "Гав"


class Cat(Animal):
  def say(self):
    return "Мяу"


dog = Dog("Бобик")
cat = Cat("Мурзик")

animal_talking(dog)
print()
animal_talking(cat)