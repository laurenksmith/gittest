# last bit of Thursday's learning Tommy wanted to go over

# def print_every_number(*tuple_of_number):  # tells us that this parameter can take more than one element (arguments) here)
#     for arg in tuple_of_number:
#         print(arg)
#
#
# print_every_number(1, 2, 3, 4, 5)

# default values:

def addition(int1=1, int2=2): # use =1 (as an example) as a default value, so that if the user does not enter the
                              # information, it will not return an error message
    return int1 + int2


print(addition())


# Library Modules and Packages