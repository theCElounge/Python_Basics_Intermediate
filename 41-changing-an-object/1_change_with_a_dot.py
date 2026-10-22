class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

pet1 = Pet("Max", 3)
pet2 = Pet("Luna", 2)
pet1.age = 4
print(pet1.age, pet2.age)

# Output:
#   4 2
