# from here we will run all application functionality

from animal import Animal
from reptile import Reptile
from snake import Snake

# abstraction
# cat = Animal()
# cat.breathe()
# print(type(cat))
# print(cat.alive)

# inheritance
# jeremy_the_reptile = Reptile()
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

print(samantha_the_snake.__venom)