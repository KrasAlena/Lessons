# greet = "Hello World"
# print(type(greet))
#
# number = 2022
# print(type(number))
#
# my_list = [1, 2, 3]
# print(type(my_list))
#
# print(type(my_list[0]))
#
# print(round(1.555, 2))
#
# my_list = ["Albert", "Nicola", "Thomas"]
# sorted_list = sorted(my_list)
#
# print(sorted_list)
#
# sorted_reverse_list = sorted(my_list, reverse=True)
#
# print(sorted_reverse_list)


# 1. Create a list of different types of python objects, and print all the types.
my_list =  [1, 'Max', True, {'1': 'value', '2': 'value2'}, 2.56, [1, 2, 3]]
for item in my_list:
    print(type(item))

# 2. Print all the items (from previous) separated with "|"
my_list2 =  [1, 'Max', True, {'1': 'value', '2': 'value2'}, 2.56, [1, 2, 3]]
print(*my_list2, sep='|')
# result = ''
# for item in my_list2:
#     result += str(item) + '|'
# print(result)

# 3. Create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.
original_list = [0.243, 1.678, 100.465, -0.364, 1.001]
rounded_list = []

for item in original_list:
    rounded_list.append(round(item, 2))
print(rounded_list)

# 4. Create a list with student names and sort them, print the result to the terminal.
students = ['Max', 'Adele', 'Tom', 'John', 'Kat', 'Ian', 'Sam']
print(sorted(students))

# 5. Write a program that allows user to write in any float number and then round it.

num = float(input('Enter any float number: '))
print(round(num)) if type(num) == float else print('Try again')


