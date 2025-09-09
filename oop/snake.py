# linear inheritance

from reptile import Reptile

# encapsulation. in python, not true encapsulation
class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self._cold_blooded = True  # overriding cold blooded in super class Reptile _ used to protect an attribute
        self.__venom = None  # __ also can be used to protect an attribute. Just gives warning, then actually protecting.More protected than 1 underscore

    def use_tonge_to_smell(self):
        print("Do I say it smells or tastes nice...?")

    @property  #created when I hovered over protected _cold_blooded in application_control. Means to access variable using method
    def cold_blooded(self):
        return self._cold_blooded