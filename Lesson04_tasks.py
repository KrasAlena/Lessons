# Write python program that asks user to enter name, surname, age.
# Put these values into a dictionary and print it.

# ent_name = input('Enter your name: ')
# ent_surname = input('Enter your surname: ')
# ent_age = int(input('Enter your age: '))

#my_dict = {'name': input('Enter your name: '), 'surname': input('Enter your surname: '), 'age': int(input('Enter your age: '))}

#print(my_dict)

# nested dictionary
nested_dictionary = {
    'name': 'John',
    'surname': 'Doe',
    'married': True,
    'kids': {
        'son': ['Ian', 13],
        'daughter': {
            'first': ['Mary', 6],
            'second': ['Ieva', 11]
        }
    },
    'cars': {
        1: 'BMW',
        2: 'Porsche'
    }
}

# Create a program, that would take sentences from the input and
# create a dictionary where they keys represents letters
# and values the frequency those letters appeared in those sentence.
# The program must demand that user should enter 3 or more sentences.


# sentence_length = 4
# sentences = []
# for i in range(4):
#     sentence = input("Enter you sentence").lower()
#     sentences.append(sentence)
#
#
# character_counts = {}
# for sentence in sentences:
#     for character in sentence:
#         character_counts[character] = character_counts.get(character, 0) + 1
#
# print(character_counts)

#-----------------------------------
# sentence_length = 4
# sentences = []
# for i in range(4):
#     sentence = input("Enter you sentence").lower()
#     sentences.append(sentence)
#
# character_counts = {}
# for sentence in sentences:
#     for character in sentence:
#         if character in character_counts.keys():
#             character_counts[character] += 1
#         else:
#             character_counts[character] = 1
# print(character_counts)

#_________________________________________
student_grades = {
    'Alex': 37,
    'Sam': 48,
    'Jack': 87,
    'Lily': 79,
    'John': 81,
    'Ann': 82,
    'Leslie': 45,
    'Paul': 93
}

grades = list(student_grades.values())


avg_grade = sum(grades) / len(grades)
print(avg_grade)

poor_students = {key for key, value in student_grades.items() if value < 80}
print(poor_students)

student_name = input('Enter a name: ')
if student_name in student_grades:
    print('This student is in this group')
else:
    print('This student isn\'t in this group')