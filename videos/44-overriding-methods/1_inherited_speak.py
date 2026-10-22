class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(self.name, "makes a sound")

class Dog(Pet):
    pass

pet1 = Dog("Max", 3)
pet1.speak()

# Output:
#   Max makes a sound
