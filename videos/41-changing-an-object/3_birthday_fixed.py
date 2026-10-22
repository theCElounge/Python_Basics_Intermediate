class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def birthday(self):
        self.age += 1

pet1 = Pet("Max", 3)
pet1.birthday()
print(pet1.age)

# Output:
#   4
