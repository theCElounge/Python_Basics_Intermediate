pet1 = {"name": "Max", "age": 3}

def describe(pet):
    print(pet["name"], pet["age"])

describe()

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   TypeError: describe() missing 1 required positional argument: 'pet'
