import sys

print("This is the name of the program: checkargs.py")
if len(sys.argv) > 1:
    args = sys.argv
    print("Number of arguments passed: {len(args)}")
else:
    print("You gave me no argument")

print("hello")


# (f"Number of arguments passed: {(len(sys.argv)-1)}"
#  (f"Argument list: {(sys.argv[1:])}")
#
#  for arg_