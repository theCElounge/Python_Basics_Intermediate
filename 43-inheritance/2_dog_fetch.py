class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} years old"

class Dog(Pet):
    def fetch(self):
        print(self.name, "fetches the ball!")

pet1 = Dog("Max", 3)
pet1.fetch()

# Output:
#   Max fetches the ball!
