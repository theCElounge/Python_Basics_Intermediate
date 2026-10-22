class Pet:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print(self.name)

pet1 = Pet("Max")
print(pet1)

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   Max
#   TypeError: __str__ returned non-string (type NoneType)
