class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describe(self):
        print(self.name, "is", self.age, "years old")

pet1 = Pet("Max", 3)
pet2 = Pet("Luna", 2)
pet1.describe()
pet2.describe()

# Output:
#   Max is 3 years old
#   Luna is 2 years old
