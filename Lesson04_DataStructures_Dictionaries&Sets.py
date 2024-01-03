from pprint import pprint

my_dictionary = {}
my_dictionary['name'] = 'Tom'

my_dictionary['surname'] = 'Doe'
print(my_dictionary['name'])

print(my_dictionary)

user_info = {
    "name": "Albert",
    "surname": "Einstein",
    "occupation": {
        "role": "Professor",
        "workplace": "University of Berlin"
    },
        "languages": ["German", "Latin", "Italian", "English", "French"]
}

for language in user_info["languages"]:
    print(language)

pprint(user_info.items())
pprint(user_info)
# print(user_info["occupation"].keys())
# print(user_info.values())

d = {'a': 10, 'b': 20, 'c': 30}
for value in d.values():
    print(value)

test_keys = ["Albert", "Tom", "Stephen"]
test_values = [1, 4, 5]
new_dictionary= dict(zip(test_keys[::-1], test_values))
print(new_dictionary)