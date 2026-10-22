class Pet:
    def __init__(self, name):
        print("Welcome,", name)

pet1 = Pet("Max")
print(pet1.name)

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   Welcome, Max
#   AttributeError: 'Pet' object has no attribute 'name'
