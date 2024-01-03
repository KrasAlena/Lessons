# Write a Python program to find the list of words that are longer than n from a given list of words.
# given_list = ['good', 'rich', 'beautiful', 'healthy', 'smart']
# new_list = []
#
# n = int(input('Enter the length: '))
#
# for item in given_list:
#     if len(item) > n:
#         new_list.append(item)
#
# print(new_list)

# Write a Python program that tells if two lists have at list one common member.
first_list = ['good', 'rich', 'beautiful', 'healthy', 'smart']
second_list = ['no', 'rich', 1, 'health', 'smartest']

for item in first_list:
    if item in second_list:
        print(f'There is a common word: {item}')