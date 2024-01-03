a = 12
b = 15


c = a + b
d = a * b
f = a / b
# print(c, d, f, sep = "\n")

# String type operations

letter = 'a'

letter2 = 'b'

name = 'Alena'

company = 'Code Academy'

age = '22'

# f stands for formatted
job_title = f'{name} works at {company}'

# print(job_title)
# print(f'{company[5:12]}{company[4:12]}')

# print(company.replace(' ', '\n'))

# Conversions
text = '0xad4'
# print(int(text, 16) * 2)
# number = int(text, 16)
# print(number)

second_number = 47.9
# print(int(second_number))

# PI = 5
#
# print(input('Enter your name:'))

# first task
name = input('Enter your name')
age = int(input('Enter your age'))
birth_year = 2023 - age
print(birth_year)

# second task
string = input('Type smth')
print(string[::-1])
print(string.upper())
print(string[1::2])

# third task
number_one = int(input('Enter the first number'))
number_two = int(input('Enter the second number'))
print(number_one * number_two)

# fourth task
string_new = input('Type smth')
print(string_new.replace('a', '@').replace('o', 'Ø'))

string1 = 'Hello! How are you?'
print(len(string1))

#5
string2 = 'restart'
modified_string2 = string2[0] + string2[1:].replace(string2[0], '$')
print(modified_string2)

#6
string = input()
if string[-3:] != 'ing':
    print(string + 'ing')
else:
    print(string + 'ly')
