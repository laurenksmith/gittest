import sys
import datetime

# sys helps us run with the Python interpreter
# helps us access the command line.
print(sys.path)   # shows us all the paths that are relevant to Python
print(sys.version)  # version of Python on my computer

print(datetime.datetime.now())

sys.argv   # python list contains command line arguments. Look into this more. Friday pm video

# check for arguments
if len(sys.argv) > 1:
    print("You gave me an argument")
else:
    print("You gave me no argument")

print("hello")