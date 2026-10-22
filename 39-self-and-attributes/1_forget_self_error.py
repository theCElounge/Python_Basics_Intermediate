class Pet:
    def __init__(name):
        print("Welcome,", name)

pet1 = Pet("Max")

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   TypeError: Pet.__init__() takes 1 positional argument but 2 were given
