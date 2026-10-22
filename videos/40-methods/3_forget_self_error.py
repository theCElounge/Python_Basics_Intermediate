class Pet:
    def describe():
        print("a pet")

pet1 = Pet()
pet1.describe()

# Output (this program stops with an error on purpose; this is the last line Python prints):
#   TypeError: Pet.describe() takes 0 positional arguments but 1 was given
