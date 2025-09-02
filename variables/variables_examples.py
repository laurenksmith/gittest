"""
Task: Python variable basics

* In your Python learning project, create a folder called 'variables', then create a new file called
'variables_examples.py' for the following tasks
*
*
*
*
*
*
*
* Overwrite the value of one of your variables which stores a number
* Check the id() of the variable before and after you overwrite the variable with a new number
* Why does the 'id' of the variable change?
* Assign one variable to another
* Start with this code: python x = 10 y = x * Check the id of x and y
* Explain why the id of x and y are the same
* What happens if after assigning x = y, I give x a different value? Does the id of y change also?
* Ask the user for some input and print the input to the screen
* Get the user's name and print to the screen
* Improve previous code to: Get name, age and DOB details from a user and print the details to the screen
* If time, improve previous code to:
    * Prompt the user and get the input on the same line
    * Print "Hi <name>" on the one line
"""
# Set/assign a variable
# Try to set a variable with a number value
a = 5

# Try to set a variable with a decimal value
b = 7.5

# Try to set a variable with a string value
c = "cheese"

# How is using '==' different?
#   Whilst '=' is used to assign a value to a variable (for example, 'a = 5' above),
#   '==' is used to check whether 2 variables have the same value. This would return a Boolean
#   value of 'True' or 'False' (for example, 'print(a == c)'  would return 'False' as the
#   a and b variables hold different values (in fact, different data types).

print(a==b)

# Print the values and data types of the variables you set values for above

print(a, (type(a)))
print(b, (type(b)))

# What does it mean that Python is...

# A strongly typed language? Compare to a weakly typed language. Include a code example
#   This means that, in Python, not only do variables have a type., but the type is really important as it impacts
#   what operations can be performed on specific variables.

# A dynamically typed language? Compare to a statically typed language. Include a code example
#   This means that the variable types can be selected and verified whilst the program is already running. It also
#   means that the variable type can be changed even whilst the program is running, which makes writing code easier.

pet = "cat"
print(type(pet))

#   As you can see in this example, I did not explicitly have to tell Python what data type pet is - it
#   is able to identify the data type itself when I run the code.

