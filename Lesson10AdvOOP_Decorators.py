class Person:
    def __init__(self, name, age, friends):
        # Direct setting
        # self._name = name
        # self._age = age
        # self._friends = friends
        # Property setting (using data validation potentially!)
        self.name = name
        self.age = age
        self.friends = friends

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n: str):
        self._name = n

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a: int):
    # Data validation
        if 0 <= a <= 150:
            self._age = a
        else:
            raise ValueError("Age is not valid!")

    def del_age(self):
        self._age = None

    @property
    def friends(self):
        return self._friends

    @friends.setter
    def friends(self, friend_list: list):
        # Data validation
        for friend in friend_list:
            if not isinstance(friend, str):
                raise ValueError(f"{friend} is not string!")
            if len(friend) == 0:
                raise ValueError("There is a friend with no name!")
        self._friends = friend_list.copy()

    def del_friends(self):
        self._friends = []


pers1 = Person("Paulius", 12, ["john", "mary"])
pers2 = Person("John", 22, ["paulius"])
# pers1.age = -2
print(pers1.name, pers1.age, pers1.friends)
pers1.del_age()
pers1.del_friends()
print(pers1.name, pers1.age, pers1.friends)

#**************************************************************************************
# EXERCISE 1
# Write a Temperature class that has a celsius property and a fahrenheit property. The
# celsius property stores the temperature in Celsius, and the fahrenheit property stores
# the temperature in Fahrenheit. The fahrenheit property should be a computed property
# that converts the Celsius temperature to Fahrenheit.
#**************************************************************************************
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


temp = Temperature(100)
print(f'Temperature in Celsius: {temp.celsius} °C')
print(f'Temperature in Fahrenheit: {temp.fahrenheit} °F')

#**************************************************************************************
# EXERCISE 2
# Write a User class that has a password property. The password property should be a
# computed property that checks whether the password is strong enough. A password is
# considered strong if it has at least 8 characters, contains at least one uppercase
# letter, one lowercase letter, and one number.
#**************************************************************************************
class User:
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, user_password: str):
        if len(user_password) < 8:
            raise ValueError('Password length should be at least 8-symbol long')

        if not any(char.isupper() for char in user_password):
            raise ValueError('Password should contain at least 1 upper case letter')

        if not any(char.islower() for char in user_password):
            raise ValueError('Password should contain at least 1 lower case letter')

        if not any(char.isdigit() for char in user_password):
            raise ValueError('Password should contain at least 1 number')

        self._password = user_password


user = User()

user.password = 'Strongpassword1'
# user.password = '1234'
print(user.password)

