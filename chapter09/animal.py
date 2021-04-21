class Animal(object):
  """docstring for Animal"""
  def __init__(self, name = "Йети"):
    super(Animal, self).__init__()
    self.name = name

  def say(self):
    raise RuntimeError("не знаю, как говорить")


def animal_talking(animal):
  print(f'{animal.name} говорит: {animal.say()}')
    