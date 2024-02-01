# def get_foo(self):
#     # Optional checks for <varname> or some other logic
#     # for getting the variable
#
#     return self._foo
#
# def set_foo(self, foo):
#     # Optional checks for <varname> or some other logic
#     # for setting the variable
#
#     self._foo = foo
class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        if self._is_age_verified(age):
            self._age = age
        else:
            raise ValueError("Age is not an integer or 0 <= x <= 150")
    def get_name(self) -> str:
        return self._name
    def set_name(self, name: str):
        self._name = name
    def get_age(self) -> int:
        return self._age
    def _is_age_verified(self, age: int) -> bool:
        # Perform reasonable checks for age
        if not isinstance(age, int):
            print("Age is not an integer!")
            return False
        if age < 0:
            print("Age cannot be negative!")
            return False
        if age > 150:
            print("People cannot get older than 150 years!")
            return False
        return True
    def set_age(self, age: int):
        if self._is_age_verified(age):
            self._age = age

pers1 = Person("Alice", 12)
# print(pers1.name)
# print(pers1.age)
print(pers1.get_name())
print(pers1.get_age())
pers1.set_age(24)
print(pers1.get_age())

pers2 = Person("Bob", 33)
print(pers2.get_name())
print(pers2.get_age())

#**************************************************************************************
# EXERCISE 1
#
# Nasa needs to calculate expenses for the new mission: using OOP principles implement
# Base and Space Shuttle classes. Create a simple calculator with:
#
# Base class should give a functionality to know info about spacecraft (age, cost,
# year built, weight etc.. ).
# Through the main class you should be able to calculate the mission cost which
# includes: fuel cost (FUEL_COST x BURN_RATE (kg/mile) * BURN_RATE_VARIABLE (2500 /
# orbit_height(in miles))) , average personals expenditures ( ppl x base_salary ).
# Prepare the final report in the file document and on screen with a method
# get_full_report with all gathered and calculated data.
#**************************************************************************************
from abc import ABC, abstractmethod
import datetime

class Base(ABC):
    def __init__(self, org, cost, year_built, weight):
        self.org = org
        self.cost = cost
        self.year_built = year_built
        self.weight = weight

    @abstractmethod
    def get_full_report(self):
        raise NotImplementedError('Subclasses must implement the get_full_report method')

    def get_current_year(self):
        current_year = datetime.datetime.now().year
        return current_year

    def get_age(self):
        return self.get_current_year() - self.year_built


class SpaceShuttle(Base):
    def __init__(self, org, cost, year_built, weight, fuel_cost, orbit_height, personnel_count, base_salary):
        super().__init__(org, cost, year_built, weight)
        self.fuel_cost = fuel_cost
        self.orbit_height = orbit_height
        self.personnel_count = personnel_count
        self.base_salary = base_salary

    def get_burn_rate(self):
        return self.weight / self.orbit_height

    def get_burn_rate_var(self):
        return 2500 / self.orbit_height

    def get_fuel_cost(self):
        return self.fuel_cost * self.get_burn_rate() * self.get_burn_rate_var()

    def get_personnel_expenditures(self):
        return self.personnel_count * self.base_salary

    def calculate_mission_cost(self):
        fuel_cost = self.get_fuel_cost()
        total_cost = self.cost + fuel_cost + self.get_personnel_expenditures()
        return total_cost

    def get_full_report(self):
        report = f'Organization: {self.org}\n'
        report += f'Year Built: {self.year_built}\n'
        report += f'Age: {self.get_age()} years\n'
        report += f'Weight: {self.weight} kg\n'
        report += f'Orbit Height: {self.orbit_height} miles\n'
        report += f'Personnel Count: {self.personnel_count}\n'
        report += f'Burn Rate: {self.get_burn_rate():,.2f} kg/mile\n'
        report += f'Mission Cost: ${self.calculate_mission_cost():,.2f}\n'

        with open('mission_report.txt', 'w') as file:
            file.write(report)

        return report


shuttle = SpaceShuttle(org='NASA', cost=1000000000, year_built=2015, weight=50000, fuel_cost=50, orbit_height=300, personnel_count=10, base_salary=70)
full_report = shuttle.get_full_report()
print(full_report)


