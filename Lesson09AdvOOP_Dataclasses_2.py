from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int = 18
    gender: str = 'male'


p1 = Person('John')
print(p1)  # Person(name='John', age=18, gender='male')

p2 = Person('Jane', 25, 'female')
print(p2)  # Person(name='Jane', age=25, gender='female')

