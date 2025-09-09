# linear inheritance

from reptile import Reptile

# encapsulation. in python, not true encapsulation
class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.cold_blooded = True  # overriding cold blooded in super class Reptile _ used to protect an attribute
        self.venom = None  # __ also can be used to protect an attribute. Just gives warning, then actually protecting.More protected than 1 underscore

    def use_tongue_to_smell(self):
        print("Do I say it smells or tastes nice...?")


