class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

pet1 = Pet("Max", 3)
print(pet1)

# Output (the number after 0x is a memory address, so it changes on every run):
#   <__main__.Pet object at 0x7f1ec8dff710>
