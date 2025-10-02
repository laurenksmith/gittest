# Abstraction example

class Animal:   # Use capital letter to name class

    def __init__(self):  # init method defines that we can create an object from this. self means referring to itself
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print('Breathe one breath in, one breath out.')

    def eat(self):
        print('Nom nom nom nom.')

