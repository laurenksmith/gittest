# inheritance - mechanism that allows class to inherit characteristics from another class.
# Eg all reptiles are animals, but not all animals are reptiles.
# Super class and sub class best naming rather than parent and child

from animal import Animal

class Reptile(Animal): # This tells us that all reptiles are animals - subclass of Animal
    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None  # Not all reptiles are tetrapods

    def seek_heat(self):
        print("It's cold out, where's the sun?")

    def use_venom(self):
        print("If I've got it, I'm using it.")