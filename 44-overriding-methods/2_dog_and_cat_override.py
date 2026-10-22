class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(self.name, "makes a sound")

class Dog(Pet):
    def speak(self):
        print(self.name, "says Woof!")

class Cat(Pet):
    def speak(self):
        print(self.name, "says Meow!")

pet1 = Dog("Max", 3)
pet1.speak()
pet2 = Cat("Luna", 2)
pet2.speak()

# Output:
#   Max says Woof!
#   Luna says Meow!
