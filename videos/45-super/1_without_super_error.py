class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Pet):
    def __init__(self, name, age, breed):
        self.breed = breed

pet1 = Dog("Max", 3, "Beagle")
print(pet1.breed)
print(pet1.name)

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   Beagle
#   AttributeError: 'Dog' object has no attribute 'name'
