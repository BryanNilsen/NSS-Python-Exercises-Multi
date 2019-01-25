class Animal:
  def sayAnimal(self):
    return "I am an animal."

class AnimalFriend:
  def sayFriend(self):
    return "My friend is Mr. Farmer"

class Cow(Animal, AnimalFriend):
  def sayCowThing(self):
    print(f"{self.sayAnimal()} {self.sayFriend()}")


# class Lion(Animal): would not inherit from AnimalFriend

bossy = Cow()
bossy.sayCowThing()

# =========

class Flying:
  def __init__(self):
    self.can_fly = True

  @property
  def wings(self):
    try:
      return self.__wing_count
    except AttributeError:
      return 2

  @wings.setter
  def wings(self, count):
    if isinstance(count, int):
      self.__wing_count = count
    else:
      raise TypeError("Wing count must be a number")

  def fly(self):
    print("I love to fly above the clouds")

class Swimming:
  def __init__(self):
    self.can_swim = True

  def swim(self):
    print("I want to swim like a penguin, in the sea.")


class Running:
  def __init__(self, leg_length):
    self.can_run = True
    self.run_speed = 2.0
    self.leg_length = leg_length

  def run(self):
    if self.leg_length < 10 and self.run_speed <= 2.0:
      return "I'm waddling as fast as I can."
    elif self.leg_length < 20:
      return "I'm running now but get closer and I'll fly instead."
    else:
      return "Catch me if you can."


class Bat(Flying):
  def __init__(self, species):
    self.has_feathers = False
    self.species = species
    super().__init__()


class Bird:
  def __init__(self, species, nest="tree"):
    self.has_feathers = True
    self.species = species
    self.nest = nest

  def layEgg(self):
    if self.nest == "tree":
      return "Sit on eggs in nest."
    else:
      return "Stand in place and sit on egg."



class Penguin(Bird, Running, Swimming):
  def __init__(self, species, nest="ground", leg_length=5):
    self.color = "black and white"

    Bird.__init__(self, species, nest)
    Swimming.__init__(self)
    Running.__init__(self, leg_length)

  def __str__(self):
    return f"can_run: {self.can_run}, can_swim: {self.can_swim}, has_feathers: {self.has_feathers}"

class Pigeon(Bird, Flying):
  def __init__(self, species, color, nest="tree"):
    self.color = color

    Bird.__init__(self, species, nest)
    Flying.__init__(self)

  def __str__(self):
    return f"can_fly: {self.can_fly}, nest_location: {self.nest}"

# Emu class inherits from Bird and Running
class Emu(Bird, Running):
  # adds color attribute
  def __init__(self, species, color, nest="ground", leg_length=20):
    self.color = color

    Bird.__init__(self, species, nest)
    Running.__init__(self, leg_length)

  def __str__(self):
    return f"can_run: {self.can_run}, leg_length: {self.leg_length}, has_feathers: {self.has_feathers}"



# create instance of a penguin
emperor_penguin = Penguin("Emperor Penguin")
print("Our running, swimming, feathery penguin:", emperor_penguin)
print(emperor_penguin.run())

# create instance of a bat
fruit_bat = Bat("Fruit Bat")
print(fruit_bat.__dict__)

common_pigeon = Pigeon("Common Pigeon", "gray")
print(common_pigeon.__dict__)
print("pigeon string: ", common_pigeon)

emu = Emu("Emu", "black and brown")
print("I am an emu: ", emu)
print("I'm an emu and I'm running.", emu.run())


