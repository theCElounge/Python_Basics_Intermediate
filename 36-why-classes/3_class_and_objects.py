class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describe(self):
        print(self.name, self.age)

pet1 = Pet("Max", 3)
pet2 = Pet("Luna", 2)
pet1.describe()
pet2.describe()

# Output:
#   Max 3
#   Luna 2
