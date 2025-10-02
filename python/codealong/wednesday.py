"""
new_string = 'hello world!'
print(new_string)

# string slicing
print(len(new_string))
print(new_string[11])
print(new_string[-1])

print(new_string[6:])
print(new_string[:6]) # this is a non exclusive way which means that it says go up to index 6 but doesn't include it
print(new_string[-3:]) # this tells it to take everything from the 3rd last character to the last character in the index
"""

example_text = "here is sOMe text with some WORDS of text."
substring = "text"

# count how many times the substring "text" appears in example_text string
"""
print(example_text.count(substring))
print(example_text.lower())
print(example_text.upper())
print(example_text.capitalize())

print(example_text.replace("with", ","))

# string concatenation

a = 2
b = 5.4
c = "there are numbers here"

print(a + b + c)
print(str(a) + str(b) + c)
"""
# # string formatting
#
# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall.") # curly braces used to bring in the variables. f shows formatting
# print(f"{name} is {years + 1} years old and {height_cm} cm tall.")
#
# pi = 3.1415926359
#
# print(f"Pi to 3 decimal places is {pi:.3f}.") # :.3f tells it to leave it to 3 decimal places. Always inside curly brackets.
# print(f"Pi to 5 decimal places is {pi:.5f}.")

hi = "Hello World!"

# print(hi.isalpha())
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith("o"))
# print(hi.startswith("Hel"))

# print(bool("")) # omitted values return false
# print(bool("a")) # all strings return true
# print(bool("ZEBRA"))
# print(bool(False)) # False returns False
# print(bool(10)) # integers return True
# print(bool(0)) # omitted value, therefore false

# None
# None is an object

x = None

print(x == False)
print(x == True)
print(x == None)
print(x is None) # preferred way of checking. More accurately able to identify objects
print(type(x))