"""
The task
Core:
Make a new 'fizzbuzz.py' file
Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz" instead of the number
For numbers which are multiples of both three and five print "FizzBuzz".
If time:
Improve the script so the user can decide which numbers to substitute for "Fizz" and "Buzz"
Refactor using functions

Acceptance Criteria
All core task done
Works with no errors
"""

# fizzbuzz.py


def fizzbuzz(start, end, fizz_num=3, buzz_num=5):
    for i in range(start, end + 1):
        if i % fizz_num == 0 and i % buzz_num == 0:
            print("FizzBuzz")
        elif i % fizz_num == 0:
            print("Fizz")
        elif i % buzz_num == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    use_custom = input("Do you want to choose your own Fizz and Buzz numbers? (Y/N): ").strip().lower()

    if use_custom == "y":
        fizz_num = int(input("Enter a number for Fizz: "))
        buzz_num = int(input("Enter a number for Buzz: "))
        fizzbuzz(1, 100, fizz_num, buzz_num)
    else:
        fizzbuzz(1, 100)  # default fizz=3, buzz=5
