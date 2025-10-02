"""
Task: Mix all the data about a user into a list
🎯 Outcome (By doing this you should): Learn how to save a mix of data types into a list

Use your code from the "Task: Python variable basics" (last subtask) where you asked the user for their name, age and DOB.
Mix the name, age and DOB into one list user_details_list
Print the user's name, age and DOB from the list
Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
Ask the user for their height in cm and save it to the variable height
Save height as a float in the list, and print the height from the list.
"""
# name = input('\nWhat is your name? ').capitalize()
# print('Lovely to meet you,', name + '.')
# age = int(input('\nMay I ask how old you are? '))
# print(str(age) + '! You do not look a day over 21.')
# dob = input('\nWhat is your date of birth? Please enter this in DD/MM/YYYY format. ')
# print('You have said your birthdate is: ', dob + '.')
#
# user_details_list = [name, age, dob]
# print(user_details_list)
#
# height = float(input('\nHow tall are you? Please give your answer in cms (without any letters). '))
#
# user_details_list.append(height)
# print(user_details_list)
"""
Task: Test you can slice lists
🎯 Outcome (By doing this you should): Learn how to slice lists

You have probably already covered string slicing
# List slicing is similar, except we are cutting up a list of item rather than a string of characters
# Starting code:
# """
# # mixture = [1, 2, 3,"one", "two", "three"]
# #
# # print(mixture)
# """
# Print these list slices to the screen:
# * Returns the 2nd and 3rd items in the list -> It should return [2, 3]
# * Returns every second item in the list -> It should return [1, 3, 'two']
# * Start at the last item, stop at the 3rd last item, and step in reverse order -> It should return ['three', 'two']
# """
# # print(mixture[1:3])
# # print(mixture[::2])
# # reverse_mixture = mixture[::-1]
# # print(reverse_mixture[0:2])
# """
# Tuples
# Task: Learn tuples - finish the "Stranded on a Desert Island" game
# 🎯 Outcome (By doing this you should): Learn how to use tuples and how they are different to lists
#
# Before finishing the game below, answer these questions:
# * How are tuples similar to lists?
#     Tuples are similar to lists in that they are an ordered collection and they allow duplicates.
#     They also start at the index [0]. Tuples, like lists, can also hold different data types.
#
# * Are tuples immutable and what does this mean?
#     Yes, they are immutable. This means they are fixed and you can't change them, unlike a list.
#
# * What other data types are immutable?
#     strings and integers.
#
# * What are good use cases for tuples instead of lists?
#     A good use case for tuples instead of lists would be if you needed to ensure that a collection of objects could not
#     accidentally be saved over, or changed. For example, a teacher keeping track of their class's marks, or
#     payroll keeping a list of employees.
#
# * What does the following piece of code do?
# """
# # python essentials = ("bread", "eggs", "milk")
# #
# # print(essentials) print(essentials.count("bread"))
#
# """
#     It returns a syntax error because Python does not recognise spaces in names. So python essentials should
#     have been python_essentials (best practice)
#
# The task
#
# Add your code where it says 'YOUR CODE GOES HERE'
#
# Starting code:
#
# # "Stranded on a Desert Island" game
# # Rationale: Practice tuples
# # Type of exercise: Finish the code
#
# """
# print("You are stranded on a desert island. You can take only THREE items.")
# essential_item1 = input("What is an essential item you would take? ")
# essential_item2 = input("What is an essential item you would take? ")
# essential_item3 = input("What is an essential item you would take? ")
# # save the items as a tuple
# essentials_tuple = (essential_item1, essential_item2, essential_item3)
# # print the tuple
# print("Here are your items as a tuple:", essentials_tuple)
# print("")
# print("I lied. You can take one more item.")
# essential_item4 = input("What is one more essential item you would take? ")
# # try to add the 4th item to the tuple
# # if you can't add the 4th item, work out how to save the 4th item to the tuple
# # additional_tuple = (essential_item4,)
# # final_essentials_tuple = (essentials_tuple + additional_tuple)
# # Discovered a quicker way to achieve the above
# # print("Here are your items as a tuple (with the 4th item added):", final_essentials_tuple)
#
# final_essentials_tuple = (essential_item1, essential_item2,essential_item3, essential_item4)
# print("Here are your items as a tuple (with the 4th item added):", final_essentials_tuple)