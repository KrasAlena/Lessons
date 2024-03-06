# **************************************************************************************
# EXERCISE 1
# Create an app that:
#
# Would create a file "Text.txt" with the full text obtained by running "import this" in the python code.
# Would print the text from the created file
# It would add today's date and time to the last line of the created file
# Numbered lines of text (a number added at the beginning of each).
# In the created file, the line "Beautiful is better than ugly." would change to "Beautiful is better than ugly."
# Would print the entire text of the file in reverse
# It would print the number of words, numbers, uppercase and lowercase letters in the text of the file
# It would copy all the text of the created file to the new file, in UPPERCASE letters only
# **************************************************************************************
import os

with open('text.txt', 'w') as file:
    file.write('''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!''')

with open('text.txt', 'r') as file:
    print(file.read())

from datetime import datetime
with open('text.txt', 'a') as file:
    file.write(f'\nToday\'s date and time: {datetime.now()}')


with open('text.txt', 'r') as file:
    lines = file.readlines()


with open('text.txt', 'w') as file:
    for index, line in enumerate(lines, 1):
        file.write(f'{index}. {line}')


with open('text.txt', 'r') as file:
    text = file.read()
    new_text = text.replace('1. Beautiful is better than ugly.', '1. Gražu yra geriau nei bjauru.')

with open('text.txt', 'w') as file:
    file.write(new_text)

with open('text.txt', 'r') as file:
    print(file.read()[::-1])

# It would print the number of words, numbers, uppercase and lowercase letters in the text of the file
with open('text.txt', 'r') as file:
    text = file.read()
    words = len(text.split())
    numbers = len([num for num in text if num.isdigit()])
    uppercase = len([letter for letter in text if letter.isupper()])
    lowercase = len([letter for letter in text if letter.islower()])
    print(f'Words: {words}\nNumbers: {numbers}\nUppercase letters: {uppercase}\nLowercase letters: {lowercase}')

# It would copy all the text of the created file to the new file, in UPPERCASE letters only
with open('text.txt', 'r') as file:
    text = file.read()
    with open('new_text.txt', 'w') as new_file:
        new_file.write(text.upper())


with open('new_text.txt', 'r') as new_file:
    print(new_file.read())


# **************************************************************************************
# EXERCISE 2
# Create an app that:
#
# Allow the user to enter the desired number of lines
# Allow the user to enter the desired name of the file to be created
# Writes the entered text as separate lines to a file
# Advices:
#
# Create a while loop that will end only when the user enters an empty line (by pressing ENTER)
# **************************************************************************************

def file_creator():
    lines = []
    while True:
        line = input('Enter a line (or press ENTER to finish): ')
        if not line:
            break
        lines.append(line)

    filename = input('Enter the name of the file to be created: ')
    if not filename:
        filename = 'user_text.txt'

    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

file_creator()

# **************************************************************************************
# EXERCISE 3
# Create an app that:
#
# Create a directory "New Directory" on the computer's desktop (Desktop)
# A text file containing today's date and time would be created in this directory
# Prints the creation date and size in bytes of this text file
# Advices:
#
# The file creation date can be accessed via os.stat("File.txt").st_ctime
# **************************************************************************************
import os
from datetime import datetime

os.chdir('/Users/alena.krasinskiene/Desktop')

desktop_path = '/Users/alena.krasinskiene/Desktop'
new_directory_path = os.path.join(desktop_path, 'NewDirectory')

if not os.path.exists(new_directory_path):
    os.mkdir(new_directory_path)
    print(f'Created directory: {new_directory_path}')

current_datetime = datetime.now()
date_time_str = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')

file_path = os.path.join(new_directory_path, f'file_{date_time_str}.txt')

with open(file_path, 'w') as file:
    file.write(f'Today\'s date and time: {current_datetime}')

file_stat = os.stat(file_path)
creation_date = datetime.fromtimestamp(file_stat.st_ctime)
file_size = file_stat.st_size

print(f'File created on: {creation_date}')
print(f'File size: {file_size} bytes')

# **************************************************************************************
# EXERCISE 3
# Create a mini-budget program that:
#
# Allow the user to enter income or expenses (with a "-" sign)
# Income and expenses would be stored in a list, and the list in a pickle file (after
# closing the program, the entered data would not disappear)
# It would reflect the income and expenses already entered
# The balance sheet of entered income and expenses will be displayed (all income and
# expenses will be added up)
# **************************************************************************************
import pickle
import os

def load_finances():
    if os.path.exists('finances.pkl'):
        with open('finances.pkl', 'rb') as file:
            return pickle.load(file)
    return {'incomes': [], 'expenses': []}

def save_finances(finances):
    with open('finances.pkl', 'wb') as file:
        pickle.dump(finances, file)

def main():
    finances = load_finances()

    while True:
        print('\nWhat do you want to enter?')
        print('1 - Income')
        print('2 - Expense')
        print('3 - Display Finances')
        print('0 - Exit')
        action = input('Enter your choice: ')

        if action == '1' or action == '2':
            amount = float(input(f"Enter the amount of {'income' if action == '1' else 'expense'}: "))
            finances['incomes' if action == '1' else 'expenses'].append(amount)
            save_finances(finances)
        elif action == '3':
            print('Current Finances:')
            print('Incomes:', finances['incomes'])
            print('Expenses:', finances['expenses'])
            print('Balance:', sum(finances['incomes']) - sum(finances['expenses']))
        elif action == '0':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()


