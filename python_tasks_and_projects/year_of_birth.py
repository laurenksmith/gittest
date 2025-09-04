from datetime import timedelta
from datetime import datetime
"""
Task: Calculate Year of Birth
Timings
30-60 Minutes

Summary
Write a Python script to calculate the user's year of birth.

The task

Acceptance Criteria
program defines the variable age_int and name_str
program prints the string "OMG <person>, you are <age> years old so you were born in <year>"
"""

"""
First part
define the variables age_int and name_str (set dummy/default/initial values)
make a calculation for the year in which the person was born
print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values
"""


# age_int = 43
# name_str = "Kevin"
# current_year = 2025
#
# birth_year = current_year - age_int
#
# print(f"OMG {name_str}, you are {age_int} years old so you were born in {birth_year}. ")

"""
Second Part
prompt the user for inputs and assign the variable age_int and name_str
remove the initial values set
"""

#
# def birth_year(current_year, age_int):
#     return current_year - age_int


name_str = (input('\n Hello. What is your name? '))
age_int = int(input(f'\n Nice to meet you, {name_str}. How old are you? Please use numbers to input your answer. '))
birth_year = 2025 - age_int
print(f"OMG {name_str}, you are {age_int} years old so you were born in {birth_year}. ")

"""
Third Part
calculate and print out the total number of hours this person has lived
"""
hours = age_int * 8760 # this method and the method below give the same answer.

print(f" You have been alive for about {hours} hours.")

age = timedelta(days=365*age_int)
number_of_hours = age.total_seconds() / 3600

print(f" You have been alive for about {number_of_hours} hours.")
"""
If time
figure out a way to account for if the persons birthday has already happened this year or not
go look into the library 'time' to be more accurate with the hours lived
show in your script that you have evaluated the methods of calculating the hours lived to see which is more accurate
"""

birthday_string = (input('\n Has your birthday already been (2025)? Y/N: '))

if birthday_string.upper == 'N':
    actual_age = age_int + 1
else:
    actual_age = age_int

hours = actual_age


