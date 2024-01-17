#**************************************************************************************
# EXERCISE 1
# Create a simple program that would log all inputs from the terminal.
# Configs must show all additional data (time, date, level etc.)
#**************************************************************************************
import logging

#logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def log_input(user_input):
    logging.info(f'User input: {user_input}')


def main():
    print("This program logs your inputs. Type 'exit' to quit.")

    while True:
        user_input = input('Enter something: ')
        log_input(user_input)

        if user_input.lower() == 'exit':
            break

if __name__ == "__main__":
    main()

#**************************************************************************************
# EXERCISE 2
# Write a function that moves all elements of one type to the end of the list:
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
# Log out inputs and results in a file.
#**************************************************************************************
import logging
logging.basicConfig(level=logging.DEBUG, filename='move_el_log.log', filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
def move_el(list, el):
    result_list = []
    for x in list:
        if x != el:
            logging.debug(f'Element {x} doesn\'t equal {el}, keeping it in the list.')
            result_list.append(x)
    for x in list:
        if x == el:
            logging.debug(f'Moving element {el} to the end of the list.')
            result_list.append(x)
    return result_list

list = [1, 3, 2, 4, 4, 1]
el = 1
print(move_el(list, el))

#**************************************************************************************
# EXERCISE 3
# Create 3 functions, that are related to each other (one is being called in another),
# and test all logger severity levels by your own design.
#**************************************************************************************
import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

lst = [1, 2, 2.5, 100, 13, 1.5, 6, 7, 8, 9]
'''3. Function that checks if all elements are numbers'''
def are_all_numbers(lst: list):
    for i in lst:
        logging.debug(f'{i}, {type(i)}')
        if not (isinstance(i, int) or isinstance(i, float)):
            logging.info(f'{i} is not a number: {type(i)}')
            return False
    logging.info(f'{lst} has all number elements')
    return True

print(are_all_numbers(lst))

'''2. Function that checks whether a list 10 elements long, all elements are numbers'''

def ten_el_long(lst):
    if are_all_numbers(lst):
        logging.info(f'The list length is {len(lst)}')
        if len(lst) < 10:
            return False
        return True
    return False

print(ten_el_long(lst))

'''1. Function that sorts a list (at least 10 element long) of numbers'''
def sort_list(lst):
    if ten_el_long(lst):
        return sorted(lst)
    logging.error(f'The list is less than 10 elements long')

print(sort_list(lst))

#**************************************************************************************
# EXERCISE 4
# Create a program that takes 4 data types/structures: strings, numbers, list, dict.
# Iterate 10 times with inputs and log what data type/structure
# and how many times was entered. Handle all possible errors and log it.
#**************************************************************************************



