import math

print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]


# A1a:

print(x[:5])

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:

even_numbers = [a for a in x if a % 2 == 0]

print(even_numbers)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:

even_numbers = [a for a in x[:5] if a % 2 == 0]

print(even_numbers)
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

new_list = [name[0] for name in names]

print(new_list)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

space_index = [name.index(" ") for name in names]

print(space_index)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

first_and_last = [n[0] + n.split()[-1][0] for n in names]

print(first_and_last)
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

for no_duplicates in list_of_lists:
    if len(no_duplicates) == len(set(no_duplicates)):
        print(no_duplicates)

# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

while True:
    try:
        user_number = int(input("Choose a number greater than 100: "))
        if user_number > 100:
            break
        else:
            print("Oops! Please only enter a number greater than 100.")
    except ValueError:
        print("Oops! That's not valid. Please enter digits only.")

# print(f"Your chosen number is: {user_number}")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:


def prime_number(n):

    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


if prime_number(user_number):
    print(f"Your chosen number is {user_number}, which is a prime number.")
else:
    print(f"Your chosen number is {user_number}, which is not a prime number.")

