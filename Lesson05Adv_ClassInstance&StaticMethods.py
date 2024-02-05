#**************************************************************************************
# EXERCISE 1
# Create a class which takes temperature measurements in Kelvins and add static methods
# to transform those to Celsius and Fahrenheit units.
#**************************************************************************************
class Temperature:
    def __init__(self, kelvins_temp):
        self.kelvins_temp = kelvins_temp

    @staticmethod
    def kelvin_to_celsius(kelvin_temp):
        celsius_temp = kelvin_temp - 273.15
        return celsius_temp

    @staticmethod
    def kelvin_to_fahrenheit(kelvin_temp):
        fahrenheit_temp = (kelvin_temp - 273.15) * 9 / 5 + 32
        return fahrenheit_temp


celsius = Temperature.kelvin_to_celsius(100)
print(f'Converted Temperature to Celsius: {celsius:.2f} °C')

fahrenheit = Temperature.kelvin_to_fahrenheit(100)
print(f'Converted Temperature to Fahrenheit: {fahrenheit:.2f} °F')

#**************************************************************************************
# EXERCISE 2
# Create a class that would take at least five imperial system measurements and would
# transform with the help of static methods to metric system units.
#**************************************************************************************
class ImperialMetricConverter:
    def __init__(self, inch, foot, pound, gallon, mile):
        self.inch = inch
        self.foot = foot
        self.pound = pound
        self.gallon = gallon
        self.mile = mile

    def get_inch_measurement(self):
        return self.inch

    def get_foot_measurement(self):
        return self.foot

    def get_pound_measurement(self):
        return self.pound

    def get_gallon_measurement(self):
        return self.gallon

    def get_mile_measurement(self):
        return self.mile

    @staticmethod
    def inches_to_meter(inch: float):
        meter = inch * 0.0254
        return meter

    @staticmethod
    def foot_to_centimeter(foot: float):
        centimeter = foot * 30.48
        return centimeter

    @staticmethod
    def pound_to_kilogram(pound: float):
        kilogram = pound * 0.453592
        return kilogram

    @staticmethod
    def gallon_to_liter(gallon: float):
        liter = gallon * 3.78541
        return liter

    @staticmethod
    def mile_to_kilometre(mile: float):
        kilometre = mile * 1.60934
        return kilometre


converter = ImperialMetricConverter(221, 2.5, 180, 5.5, 113)

inch = converter.get_inch_measurement()
print(f'Length in inches: {inch} in')
meter = ImperialMetricConverter.inches_to_meter(inch)
print(f'Converted length to meters: {meter:.2f} m')

#**************************************************************************************
# EXERCISE 3
# Create a class called TimeUtils that has a static method called time_to_seconds that
# takes a time string in the format hh:mm:ss and returns the total number of seconds
# represented by that time. Use functional programing paradigm.
#**************************************************************************************
class TimeUnits:
    @staticmethod
    def time_to_seconds(time: str):
        arr_str = time.split(':')
        arr_num = [int(i) for i in arr_str]
        seconds = (arr_num[0] * 3600) + (arr_num[1] * 60) + arr_num[2]
        return seconds


seconds_time = TimeUnits.time_to_seconds('03:13:10')
print(f'Converted time to seconds: {seconds_time} s')

#**************************************************************************************
# EXERCISE 4
# Create a class called Employee with a static method called calculate_payroll that
# takes a list of Employee instances and returns the total amount to be paid to all
# employees. Each Employee instance has two attributes: name and salary.
#**************************************************************************************
class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    @staticmethod
    def calculate_payroll(employee_list: list):
        return sum([employee.salary for employee in employee_list])


employee1 = Employee('John', 2300)
employee2 = Employee('Sarah', 2700)

print(f'{employee1.name}\'s salary - {employee1.salary}')
print(f'{employee2.name}\'s salary - {employee2.salary}')

employee_list = [employee1, employee2]

total = Employee.calculate_payroll(employee_list)
print(f'Total to be paid: {total}')