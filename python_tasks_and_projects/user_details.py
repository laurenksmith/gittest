"""
Task: Mix all the data about a user into a list
🎯 Outcome (By doing this you should): Learn how to save a mix of data types into a list
Use your code from the "Task: Python variable basics" (last subtask) where you asked the user for their name, age and DOB.
Mix the name, age and DOB into one list user_details_list
Print the user's name, age and DOB from the list
Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
Ask the user for their height in cm and save it to the variable height
Save height as a float in the list, and print the height from the list
"""

# greeting = input('\n Hello! How are you today? ')
# print('You said:', greeting + '.')

name = input('\nWhat is your name? ').capitalize()
print('Lovely to meet you,', name + '.')
age = int(input('\nMay I ask how old you are? '))
print(str(age) + '! You do not look a day over 21.')
dob = input('\nWhat is your date of birth? Please enter this in DD/MM/YYYY format. ')
print('You have said your birthdate is: ', dob + '.')

user_details_list = [name, age, dob]
print(user_details_list)

height = float(input('\nHow tall are you? Please give your answer in cms (without any letters). '))

user_details_list.append(height)
print(user_details_list)