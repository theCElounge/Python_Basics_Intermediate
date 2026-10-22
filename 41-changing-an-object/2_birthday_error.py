class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def birthday(self):
        age += 1

pet1 = Pet("Max", 3)
pet1.birthday()

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   UnboundLocalError: cannot access local variable 'age' where it is not associated with a value
