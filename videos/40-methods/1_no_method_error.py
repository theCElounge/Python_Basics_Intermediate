class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

pet1 = Pet("Max", 3)
pet1.describe()

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   AttributeError: 'Pet' object has no attribute 'describe'
