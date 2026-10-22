class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} years old"

class Dog(Pet):
    def fetch(self):
        print(self.name, "fetches the ball!")

class Cat(Pet):
    pass

pet2 = Cat("Luna", 2)
pet2.fetch()

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   AttributeError: 'Cat' object has no attribute 'fetch'
