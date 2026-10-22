class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} years old"

pet1 = Pet("Max", 3)
print(pet1)

# Output:
#   Max, 3 years old
