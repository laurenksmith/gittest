# from here we will run all application functionality

from animal import Animal
from reptile import Reptile
from snake import Snake
from python_in_class import Python

# abstraction
cat = Animal()
# cat.breathe()
# print(type(cat))
# print(cat.alive)

# inheritance
jeremy_the_reptile = Reptile()
# jeremy_the_reptile.use_venom()
# jeremy_the_reptile.breathe()
# print(jeremy_the_reptile.alive)

# encapsulation
samantha_the_snake = Snake()
# print(samantha_the_snake.venom)
# print(samantha_the_snake.alive)
# print(samantha_the_snake.lungs)
# samantha_the_snake.venom = False
# print(samantha_the_snake.venom)

# print(samantha_the_snake.venom)
# samantha_the_snake.venom = True
# print(samantha_the_snake.venom)


# polymorphism
patricia_the_python = Python()
# cat.eat()
# patricia_the_python.eat()

animals = [cat, patricia_the_python, samantha_the_snake, jeremy_the_reptile]

for animal in animals:
    animal.eat()
