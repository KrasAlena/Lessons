#**************************************************************************************
# EXERCISE 1
# Create a simple calculus program as a script and as module.
#**************************************************************************************
import moduleL13_Ex1 as calc

print(calc.add(1, 2))
print(calc.sub(11, 3))
print(calc.prod(3, 17))
print(calc.div(13, 0))
#**************************************************************************************
# EXERCISE 2
# Create a program with 3 different modules:
#
# first, to do basic tasks with strings
# second, basic tasks with lists.
# third, basic tasks with numbers
# Import them as modules to the main.py module and show calculations.
#**************************************************************************************

#look mainL13Ex2 file


#**************************************************************************************
# EXERCISE 3
# Create a module and import any PIP package of your choice.
# Then create a function that would use it.
# Import that function to the main.py module and use it.
#**************************************************************************************
import numpy as np
def square_root_array(arr):
    return np.sqrt(arr)

# Example usage
numbers = [4, 9, 16, 25]
result = square_root_array(numbers)
print(result)



#**************************************************************************************
# EXERCISE 4
# Python's os module provides a way of using operating system dependent functionality
# such as reading or writing to the file system. Your task is to:
#
# Import the os module.
# Create a function that lists all files in the current directory.
# Create a function that creates a new directory.
# Create a function that renames a file.
# Create a function that moves a file from one directory to another.
# Create a function that deletes a file.
#**************************************************************************************