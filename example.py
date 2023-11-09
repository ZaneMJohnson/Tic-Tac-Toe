class Animal:
  def __init__(self, name) -> None:
    self.name = name
    pass

  def sound(self):
    print(f'Makes a {self.name} sound!')


if __name__ == "__main__":
  dog = Animal("Doc")
  cat = Animal("Cat")
  river_rat = Animal("Kirk")
  
  dog.sound()
  cat.sound()
  river_rat.sound()
