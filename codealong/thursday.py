"""
Sets

unordered
unindexed
so, can't search for items by index number since not indexed. Likewise, can't search for index number by item name.
does not allow duplicates

When printed, seem to come in same order every time anyway, even though considered unordered.

In the below example - it did keep changing the order!!

"""

# fruits = {"apple", "banana", "mango"}
# print(fruits)
#
# fruits.add("cherry")  # add an item
# fruits.remove("banana")  # remove an item
# fruits.add("cherry")  # does not allow duplicates
# print(fruits)
# fruits.discard("mango")  # also removes, but doesn't cause an error message if the item you are trying to remove doesn't exist.
#
# """
# frozen sets
#
# immutable sets
# """
#
# frozen_set = frozenset(["hello", "world"])
# print(frozen_set)
# # frozen_set.add("more")  # not possible - it's immutable (frozen), therefore can't add to it.
#
# frozen_normal_set = frozenset(fruits)  # can create a frozen set from a normal set
# print(frozen_normal_set)
#
# fruits.add(frozen_set)
# print(fruits)


print("\nQ1a\n")

# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


def divisors(number: int) -> list:
    divisors_list =[]
    for i in range(1, number + 1):
        if number % i == 0:  # if is a statement NOT a function
            divisors_list.append(i)
    return divisors_list
print(divisors(12))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function)

print(42 % 7 == 0 or 7 % 42 == 0)  # mine: must be in a function!!!


def is_factor(num1: int, num2: int) -> bool:
    if num2 in divisors(num1) or num1 in divisors(num2):
        return True
    else:
        return False

# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


def alphabet_position(letter:str) -> int:
    return alphabet.index(letter)


print(alphabet_position('g'))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


def id_generator(name_string: str) -> str:
    id = ""
    for letter in name_string:
        id = id + str(alphabet_position(letter))
    return id


print(id_generator("abba"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


def password_generator(name_string: str) -> str:
    number = 0
    for i in id_generator(name_string):
        number = number + int(i)  # or number += int(i) - shorthand version
    return str(int(id_generator(name_string)) - number)


print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


def is_prime(number) -> bool:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    return prime


print(is_prime(5))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


def is_prime_2(number) -> bool:
    if number.isdigit():
        return is_prime(number)
    else:
        print("Please enter a digit")

print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

counter = 1
for number in x:
    if counter <= 5:
        print(number)
        counter += 1


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)

for number in x:
    if number % 2 == 0:
        print(number)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)


counter = 1
for number in x:
    if counter > 5:
        break
    elif number % 2 == 0:
        print(number)
    counter += 1


print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

initial = []
for name in names:
    initial.append(name[0])
print(initial)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

space_index = []
for name in names:
    space_index.append(name.index(" "))
print(space_index)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

initials = []
for name in names:
    initials.append(name[0] + name[name.index(' ') + 1])
print(initials)
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

no_duplicates = []
for i in list_of_lists:
    if len(set(i)) == len(i):
        no_duplicates.append(i)
print(no_duplicates)

# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

user_prompt = True
number = 0
while user_prompt:
    number = input("Enter a number greater than 100: ")
    if number.isdigit():
        if int(number) > 100:
            user_prompt = False

print(number)


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:


user_prompt = True
number = 0
while user_prompt:
    number = input("Enter a number greater than 100: ")
    if number.isdigit():
        if int(number) > 100:
            user_prompt = False

        prime = True
        for i in range(2, int(number)):
            if number % i == 0:
                prime = False
        if prime:
            print("prime")
        else:
            print("not prime")


