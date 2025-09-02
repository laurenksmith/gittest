"""
Task: Python variable basics

1. Set/assign a variable
2. Try to set a variable with a number value
a = 5

3. Try to set a variable with a decimal value
b = 7.5

4. Try to set a variable with a string value
c = "cheese"


5. How is using '==' different?
    Whilst '=' is used to assign a value to a variable (for example, 'a = 5' above),
    '==' is used to check whether 2 variables have the same value. This would return a Boolean
    value of 'True' or 'False' (for example, 'print(a == c)'  would return 'False' as the
    a and b variables hold different values (in fact, different data types).

print(a==b)

6. Print the values and data types of the variables you set values for above

print(a, (type(a)))
print(b, (type(b)))

7. What does it mean that Python is a strongly typed language? Compare to a weakly typed language. Include a code example.
    This means that, in Python, not only do variables have a type, but the type is really important as it impacts
    what operations can be performed on specific variables. It also refers to the fact that the type won't change
    unexpectedly.

city = "London"
print(type(city))

    In the example above, Python will return the data type as a string each time we run the code, and we would
    not expect it to return, for example, 'integer' at all.
    JavaScript is considered a weakly typed language because it is able to automatically switch between data types,
    which can lead to errors when running operations on these valuables.

8. What does it mean that Python is a dynamically typed language? Compare to a statically typed language. Include a code example.
    This means that the variable types can be selected and verified whilst the program is already running. It also
    means that the variable type can be changed even whilst the program is running, which makes writing code
    easier/quicker.

pet = "cat"
print(type(pet))

    As you can see in this example, I did not explicitly have to tell Python what data type pet is - it
    is able to identify the data type itself when I run the code.
    Java is an example of a statically typed language. This means that, unlike Python, the data type needs to be
    decided before running the code. This is done by assigning data types to variables, for example 'int a = 5;'.
    Although this process does take longer, because the user needs to type the data types themselves, it does mean
    that statically typed languages are considered more predictable than dynamic ones.



9. Overwrite the value of one of your variables which stores a number
10. Check the id() of the variable before and after you overwrite the variable with a new number

print(id(a))

a = 25
print(id(a))


11. Why does the 'id' of the variable change?
        When a variable is created, it's value is assigned it's own unique ID number like an 'address', where it is stored in
        Python's memory. So, a's original value, 5, was created, that value (5) given it's own ID number. Although I have
        overwritten the value of 'a', it is a different value, therefore it gets it's own ID number as it is stored in a
        'place' or 'address' in Python's memory.

12. Assign one variable to another

a = b
print(a, b)


# 13. Start with this code: python x = 10 y = x
# 14. Check the id of x and y
x = 10
y = x

print('The ID number of x is: ' + str(id(x)), '\nThe ID number of y is: ' + str(id(y)))


15. Explain why the id of x and y are the same
        I believe, linked to the previous question about ID numbers, it is because, although they are 2 different variables
        (x, y), y is now using x's value, which is stored at a specific 'address' in Python's memory, located using it's
        unique ID number. So, both variables have the same value, which has one ID number.


16. What happens if after assigning x = y, I give x a different value? Does the id of y change also?
        No, it doesn't. Integers are considered Primitive Value Types, which means that they store the value directly,
        and are their own distinct copy of that value. When you change the value of x, y is not effected by that
        change because it has been assigned the value of 10, rather than the value 'x' which would make it change
        when x changes. Therefore, it keeps the ID number for 10, whilst, as you can see from my example below, x now
        has a new id number, which belongs to the value of 15. 

x = 15
print('The ID number of x is: ' + str(id(x)), '\nThe ID number of y is: ' + str(id(y)))

# 17. Ask the user for some input and print the input to the screen
# 18. Get the user's name and print to the screen
greeting = input('\n Hello! How are you today? ')
print('You said:', greeting + '.')
name = input('\nWhat is your name? ').capitalize()
# print("Lovely to meet you,", name + '.')

# 19. Improve previous code to: Get name, age and DOB details from a user and print the details to the screen
# 20. If time, improve previous code to prompt the user and get the input on the same line
# 21. If time, improve previous code to print "Hi <name>" on the one line

print('Lovely to meet you,', name + '.')
age = int(input('\nMay I ask how old you are? '))
print(str(age) + '! You do not look a day over 21.')
dob = input('\nWhat is your date of birth? Please enter this in DD/MM/YYYY format. ')
print('You have said your birthdate is: ', dob + '.')
"""

