# import the module
# from maths_operations import add
import maths_operations  # this is what Tommy says is best practice. This links with line 15. In CFG, I did the way
                         # shown on lines 2 and lines 8-11.
# # from maths_operations import *   this way imports EVERYTHING from that module.


# first_number = int(input('Enter first number: '))
# second_number = int(input('Enter second number: '))
# result = add(first_number, second_number)
# print(f"{first_number} + {second_number} = {result}")


first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
result = maths_operations.add(first_number, second_number)
print(f"{first_number} + {second_number} = {result}")