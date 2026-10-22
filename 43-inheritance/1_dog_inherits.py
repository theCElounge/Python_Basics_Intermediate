class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} years old"

class Dog(Pet):
    pass

pet1 = Dog("Max", 3)
print(pet1)

# Output:
#   Max, 3 years old
