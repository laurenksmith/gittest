import math

print("\nQ1a\n")

# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:
def number_of_divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors


print(number_of_divisors(36))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function)

# A1b:

# I need to work out if an integer is a factor of a second integer, or vice versa
# If it is, I need to return True. If not, False.
# I know to use the % sign to see if one number divides another equally
# I need to work out how to check both ways, not just one way - 2 functions?
# I need to use Boolean
# I know there is a way to check for 2 different 'elements' and then return True or False (learnt yesterday)


print(42 % 7 == 0 or 7 % 42 == 0)


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# choose_a_letter = input("Pick any letter from the alphabet: ")
# choose_a_letter = choose_a_letter.lower()
#
# position_in_alphabet = alphabet.index(choose_a_letter) + 1
#
# print(f"Your chosen letter, '{choose_a_letter}' is in position {position_in_alphabet} in the alphabet.")

# A2a:
print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# def name_to_id():
#     name = input("Type your first name here: ").lower()
#     id_number = ""
#     for l in name:
#         index_position = alphabet.index(l) + 1
#         id_number += str(index_position)
#     return name, id_number


# A2b:
print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:


# def id_to_password(id_number):
#     sum_of_numbers = 0
#     for n in id_number:
#         sum_of_numbers += int(n)
#     password = int(id_number) - sum_of_numbers
#     return password
#
#
# name, id_number = name_to_id()
# password = id_to_password(id_number)
# print(f"Hello, {name.capitalize()}. Your ID number is: {id_number} and your password is: {password}. Have a great day!")

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:


def prime_number(n):

    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


while True:
    try:
        user_number = int(input("Choose an integer: "))
        break
    except ValueError:
        print("Oops! Please only enter integers (numbers/digits).")

result = prime_number(user_number)
print(f"Is {user_number} prime? {result}")


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:



# -------------------------------------------------------------------------------------- #