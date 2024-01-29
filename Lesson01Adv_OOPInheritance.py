#*******************************************
# multiple inheritance in Python
# #*******************************************
class Animal:
    def __init__(self, name, number_of_legs=4):
        self.name = name
        self.number_of_legs = number_of_legs

    def make_sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, 4)
        self.breed = breed

    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name, 4)
        self.fur_color = fur_color

    def make_sound(self):
        print("Meow")


# Here's an example of a class that inherits from both Dog and Cat
class DogCat(Dog, Cat):
    def __init__(self, name, breed, fur_color):
        Dog.__init__(self, name, breed )
        Cat.__init__(self, name, fur_color )



dogcat = DogCat(name="Fluffy", breed="Poodle", fur_color="White")
print(dogcat.name)  # prints "Fluffy"
print(dogcat.breed)  # prints "Poodle"
print(dogcat.fur_color)  # prints "White"
dogcat.make_sound()  # prints "Bark"


class Animal:
    def __init__(self, name, number_of_legs=4):
        self.name = name
        self.number_of_legs = number_of_legs

    def make_sound(self):
        print("some sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, 4)
        self.breed = breed

    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name, 4)
        self.fur_color = fur_color

    def make_sound(self):
        print("Meow")

class DogCat(Dog, Cat):
    def __init__(self, name, breed, fur_color):
        Dog.__init__(self, name, breed)
        Cat.__init__(self, name, fur_color)

print(DogCat.__mro__)

dogcat = DogCat(name="DogKitty", breed = "Mixed", fur_color="Black")
print(dogcat.name)
print(dogcat.breed)
print(dogcat.fur_color)
dogcat.make_sound()

#**************************************************************************************
# EXERCISE 1
'''
Define a Shape class with the following attributes and methods:

A name attribute, which is a string that represents the name of the shape.
A sides attribute, which is an integer that represents the number of sides of the shape.
An area method, which returns the area of the shape.
Then, define a Rectangle class that inherits from the Shape class and has the following attributes and methods:

A width attribute, which is a float that represents the width of the rectangle.
A height attribute, which is a float that represents the height of the rectangle.
An init method that initializes the name, sides, width, and height attributes.
An area method that overrides the area method of the Shape class and returns the area of the rectangle.
Finally, define a Square class that inherits from the Rectangle class and has the following attributes and methods:

A side_length attribute, which is a float that represents the length of the sides of the square.
An init method that initializes the side_length attribute and calls the init method of the Rectangle class to initialize the name, sides, width, and height attributes.
'''
#**************************************************************************************
class Shape:
    def __init__(self, name: str, sides: int):
        self.name = name
        self.sides = sides

    def area(self):
        raise NotImplementedError('Subclasses must implement the area method')

class Rectangle(Shape):
    def __init__(self, name: str, width: float, height: float):
        super().__init__(name, 4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, name, side_length):
        super().__init__(name, width=side_length, height=side_length)
        self.side_length = side_length

rectangle = Rectangle('rec', width=6, height=8)
square = Square('sqr', side_length=4)
print(square.area())

#**************************************************************************************
# EXERCISE 2
#
# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.
#**************************************************************************************
class Vehicle:
    def __init__(self, make, model, seating_capacity):
        self.make = make
        self.model = model
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f'Make: {self.make}, Model: {self.model}, Seating Capacity: {self.seating_capacity}')

    def start_engine(self):
        print('Engine started')

    def stop_engine(self):
        print('Engine stopped')

    def accelerate(self):
        print('Vehicle is accelerating')

    def brake(self):
        print('Vehicle is braking')

    def calculate_fare(self):
        fare = self.seating_capacity * 100
        return fare


class Bus(Vehicle):
    def __init__(self, make, model, seating_capacity):
        super().__init__(make, model, seating_capacity)

    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.1 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare


class Taxi(Vehicle):
    def __init__(self, make, model, seating_capacity):
        super().__init__(make, model, seating_capacity)


class Train(Vehicle):
    def __init__(self, make, model, seating_capacity):
        super().__init__(make, model, seating_capacity)


# Example usage:

# Create instances of the classes
bus = Bus(make='Mercedes', model='Sprinter', seating_capacity=20)
taxi = Taxi(make="Toyota", model='Camry', seating_capacity=4)
train = Train(make='Amtrak', model='Express', seating_capacity=100)

# Display information
bus.display_info()
taxi.display_info()
train.display_info()

# Calculate fares
bus_fare = bus.calculate_fare()
taxi_fare = taxi.calculate_fare()
train_fare = train.calculate_fare()

print(f'Bus fare: ${bus_fare}')
print(f'Taxi fare: ${taxi_fare}')
print(f'Train fare: ${train_fare}')

#**************************************************************************************
# EXERCISE 3
#
# Define the Animal, Mammal, and Primate classes.
# Animal should have a name attribute and a make_noise() method.
# Mammal should have a warm_blooded attribute and a give_birth() method.
# Primate should have an opposable_thumbs attribute and a swing() method.
# Test the classes by creating a Chimpanzee and making it do various things :)
#**************************************************************************************
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_noise(self):
        raise NotImplementedError('Subclasses must implement the area method')

class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool):
        super().__init__(name)
        self.warm_blooded = warm_blooded

    def give_birth(self, amount: str):
        return f'Now there\'s two of us: {amount * 2}'

class Primate(Mammal):
    def __init__(self, name: str, warm_blooded: bool, opposable_thumbs: bool):
        super().__init__(name, warm_blooded)
        self.opposable_thumbs = opposable_thumbs

    def make_noise(self):
        print('Uaaaaaa')

    def swing(self):
        print('I can swing')

chimp = Primate('Nancy', True, True)
# 🐒
# Access attributes
print(f'Chimpanzee name: {chimp.name}')
print(f'Warm-blooded: {chimp.warm_blooded}')
print(f'Opposable thumbs: {chimp.opposable_thumbs}')

# Call methods
chimp.make_noise()
print(chimp.give_birth('🐒'))
chimp.swing()

#**************************************************************************************
# EXERCISE 4
#
# Lets say we have classes: A, B and C:
#
# Modify the program to add a method say_hello to class A that prints "Hello from class A".
# Modify the program to add a method say_hello to class B that prints "Hello from class B".
# Modify the program to add a method say_hello to class C that prints "Hello from class C".
# Create an object of class C and call the say_hello method on it. What is the output?
# Modify the program so that class B's say_hello method calls the say_hello method of class A
# using the super() function.
# Create an object of class C and call the say_hello method on it again. What is the output now?
#**************************************************************************************
class A:
    def say_hello(self):
        print('Hello from class A')

class B:
    def say_hello(self):
        print('Hello from class B')

class C:
    def say_hello(self):
        print('Hello from class C')

c = C()
c.say_hello()
#-------------------------------------------
class A:
    def say_hello(self):
        print('Hello from class A')

class B(A):
    def say_hello(self):
        print('Hello from class B')
        super().say_hello()

class C(B):
    def say_hello(self):
        print('Hello from class C')
        super().say_hello()

c = C()
c.say_hello()
