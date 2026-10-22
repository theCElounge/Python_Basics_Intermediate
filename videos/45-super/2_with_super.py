class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

pet1 = Dog("Max", 3, "Beagle")
print(pet1.name, pet1.breed)

# Output:
#   Max Beagle
