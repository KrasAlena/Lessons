#*******************************************
# WHILE LOOP
#*******************************************
import random

i = 0
while i < 10:
  print(i)
  i += 1
#-------------------------------------------

while True:
    user_input = input("Enter your name: ")
    if len(user_input) != 0:
        break
print(f"You entered {user_input }")
#-------------------------------------------

while True:
    secret = "secret"
    user_input = input("Enter the secret: ")
    if user_input == secret:
        print("You're in!")
        break
    else:
        print("Sorry, try again!")

#*******************************************
# FOR LOOP
#*******************************************

names = ["Albert", "Tom", "Leonardo"]
for name in names:
    print(f"Greetings, {name}")
#-------------------------------------------

name = "Code Academy"
for character in name :
    print(character)
#-------------------------------------------

my_dict = {"name": "Albert", "role": "scientist"}

for key, value in my_dict.items():
    print(key, value)
#-------------------------------------------

names = ("Albert", "Tom", "Leonardo")
for name in names:
    print(f"Greetings, {name}")

#*******************************************
# RANGE() FUNCTION
#*******************************************

# range(start, stop, step)

x = range(3, 6)
for n in x:
  print(n)

#*******************************************
# break
#*******************************************

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#*******************************************
# continue
#*******************************************

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#**************************************************************************************
# EXERCISE 1
# Create a variables containing strings for username and password.
# Start endless loop allowing to enter username and password.
# If credentials are correct stop endless loop and print greeting message.
#**************************************************************************************
user_name = 'alex'
password = 'qwerty1'
attempts = 0

while True:
    user_input_name = input('Enter the user name: ')
    user_input_password = input('Enter the password: ')
    if user_input_name == user_name and user_input_password == password:
        print('Hello. It is nice to see you')
        break
    else:
        attempts += 1
        if attempts >= 3:
            break
        print('Try again!')

#**************************************************************************************
# EXERCISE 2
# Allow user to enter 10 integers,
# and then print the sum and average of those entered numbers.
#**************************************************************************************
user_sum = 0
for i in range(10):
    number = int(input('Enter a number: '))
    user_sum += number
print(f'Sum of your numbers equals {user_sum}. '
      f'The average of your numbers equals {user_sum / 10}')

#**************************************************************************************
# EXERCISE 3
# Generate a dictionary of 10 keys (1,2,3...10).
# Each of them should store a value of random integer number from 1 to 100.
#**************************************************************************************
import random
my_dict = {}
for key in range(1, 11):
    value = random.randint(1, 100)
    my_dict[key] = value
print(my_dict)

#**************************************************************************************
# EXERCISE 4
# Create a pin code cracker. Let's say pin code consists of 4 random digits.
# You can store the value in variable.
# Then create a loop going through all possible combinations
# until you find the one you entered.
#**************************************************************************************
import random
pin_code = random.randint(1000, 9999)

for i in range(1000, 10000):
    if i == pin_code:
        print(f'{i} is the correct pin code')
        break


#**************************************************************************************
# EXERCISE 5
# Create a program that allows a user to enter a series of numbers,
# and then calculates the average of all the numbers.
# The program should also print the list of all the numbers, as well as the average.
#**************************************************************************************
num_count = 0
user_sum = 0
num_list = []
while True:
    number = input('Enter a number: ')
    if number == '':
        break
    else:
        user_sum += int(number)
        num_list.append(int(number))
        num_count += 1

print(user_sum / num_count)
print(num_list)

#**************************************************************************************
# EXERCISE 6
# Counting Up:
# Write a program that uses a while loop to print numbers from 1 to 5.
#**************************************************************************************
i = 1
while i < 6:
    print(i)
    i += 1

#**************************************************************************************
# EXERCISE 7
# Counting Down:
# Write a program that uses a while loop to print numbers from 10 to 1.
#**************************************************************************************
i = 10
while i >= 1:
    print(i)
    i -= 1

#**************************************************************************************
# EXERCISE 8
# User Input:
# Create a program that asks the user to enter a number.
# Use a while loop to print the square of that number and ask the user
# if they want to enter another number. Continue the loop until the user chooses to exit.
#**************************************************************************************
while True:
    user_number = int(input('Enter a number: '))
    print(user_number ** 2)
    user_answer = input('Do you want to enter another number? Answer Y or N ')
    if user_answer == 'N':
        break

#**************************************************************************************
# EXERCISE 9
# Print Even Numbers:
# Write a program using a for loop to print all even numbers from 1 to 10.
#**************************************************************************************
for n in range(1, 11):
    if n % 2 == 0:
        print(n)