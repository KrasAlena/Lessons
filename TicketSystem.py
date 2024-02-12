#**************************************************************************************
# EXERCISE 5
# Create a flight ticketing mini system:
#
# The CLI should ask you to choose departure place and destination (minimum 5 cities)
# (Use dictionary to create a distance between the cities matrix map ).
# Then it should show options for at least 3 flight options with different aircraft
# (Airbus A330-300, A340-300,A 340-600, A350- 100, Boeing 747-400, 747-800, 777-300).
# Every aircraft has different seat configuration (economy, business, first with different
# seat amount, seat pitch and average price)
# When you select the ticket (the provided option) the final cost should be calculated
# depending on aircraft type, departure time, and fuel consumption. (We can agree that
# flights that are departure earlier, has less seats and older, cost more). Use data
# classes and simple classes to achieve the result.
#**************************************************************************************
from dataclasses import dataclass
from datetime import datetime
from typing import List
import calendar
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


@dataclass
class Seat:
    seat_type: str


class SeatConfiguration:
    seat_type: str
    seat_count: int
    average_price: float

    def __init__(self, seat_type: str, seat_count: int, average_price: float):
        self.seat_type = seat_type
        self.seat_count = seat_count
        self.average_price = average_price


class Aircraft:
    model: str
    seat_configurations: List[SeatConfiguration]


@dataclass
class City:
    name: str


@dataclass
class Direction:
    origin: City
    destination: City
    distance: float


class DirectionManager:
    def __init__(self):
        self.cities = []

    def add_city(self, city: City):
        self.cities.append(city)

    def add_direction(self, origin: City, destination: City):
        if origin not in self.cities or destination not in self.cities:
            print('Error: Origin or destination city does not exist.')
            return
        direction = Direction(origin, destination)
        return direction

    def get_coordinates(self, city: City):
        geolocator = Nominatim(user_agent='city_distance_calculator')
        location = geolocator.geocode(city.name)
        if location:
            return (location.latitude, location.longitude)
        else:
            print('Coordinates for ', city, 'were not found.')
            return None

    def calculate_distance(self, city1: City, city2: City) -> float:
        city1_coords = self.get_coordinates(city1)
        city2_coords = self.get_coordinates(city2)

        if city1_coords and city2_coords:
            distance = geodesic(city1_coords, city2_coords).kilometers
            return distance

    def list_directions_from_city(self, city: City):
        directions = []
        for other_city in self.cities:
            if other_city != city:
                distance = self.calculate_distance(city, other_city)
                direction = Direction(city, other_city, distance)
                directions.append(direction)
        return directions


@dataclass
class Ticket:
    date: datetime
    seat_config: str
    departure_city = None
    destination_city = None

    def set_flight_date(self):
        current_year = datetime.now().year
        month = int(input(f'Ticket booking is only available for the current year.\n'
                          f'Choose a month (a number from 1 to 12) in {current_year}: '))

        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatmonth(current_year, month)

        print(cal_str)

        day = int(input('Choose day: '))
        date = datetime(current_year, month, day)
        print(f'Chosen date: {date}')

        self.date = date.date()
        return date

    def set_flight_direction(self, manager: DirectionManager):
        print('Select departure city:')
        for i, city in enumerate(manager.cities, 1):
            print(f'{i}. {city.name}')
        departure_choice = int(input('Enter the number of the departure city: ')) - 1
        self.departure_city = manager.cities[departure_choice]

        print('Select destination city:')
        destination_cities = [city for city in manager.cities if city != self.departure_city]
        for i, city in enumerate(destination_cities, 1):
            print(f'{i}. {city.name}')
        destination_choice = int(input('Enter the number of the destination city: ')) - 1
        self.destination_city = destination_cities[destination_choice]

        return self.departure_city, self.destination_city

    def select_seat_type(self, available_seat_types: List[str]) -> str:
        print('Available seat types:')
        for i, seat_type in enumerate(available_seat_types, start=1):
            print(f'{i}. {seat_type}')
        while True:
            choice = input('Choose a seat type: ')
            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(available_seat_types):
                    selected_seat_type = available_seat_types[choice_index]
                    self.seat_config = selected_seat_type
                    return selected_seat_type
                else:
                    print('Invalid choice. Please enter a valid number.')
            except ValueError:
                print('Invalid input. Please enter a number.')

    def calculate_cost(self, seat_configurations: List[SeatConfiguration], distance: float) -> float:
        selected_seat_type = self.seat_config
        base_price = 0
        for config in seat_configurations:
            if config.seat_type == selected_seat_type:
                base_price = config.average_price
                break

        total_price = base_price

        if selected_seat_type == "Business":
            total_price *= 1.20
        elif selected_seat_type == "First":
            total_price *= 1.40

        if self.date.month == datetime.now().month:
            total_price *= 1.10
        elif (self.date - datetime.now().date()).days <= 60:
            total_price *= 1.05

        if distance <= 1500:
            total_price *= 1.05
        elif 1501 <= distance <= 3000:
            total_price *= 1.10
        elif 3001 <= distance <= 5000:
            total_price *= 1.15
        else:
            total_price *= 1.20

        return round(total_price, 3)

    def get_flight_info(self, total_price):
        print(f'Your flight info:\nDeparture: {self.departure_city.name}\nDestination: {self.destination_city.name}\n'
              f'Date: {self.date}\nSeat class: {self.seat_config}\n'
              f'Ticket price: {total_price}')


def main():
    city1 = City('New York')
    city2 = City('Los Angeles')
    city3 = City('Chicago')
    city4 = City('Houston')
    city5 = City('Miami')

    manager = DirectionManager()
    manager.add_city(city1)
    manager.add_city(city2)
    manager.add_city(city3)
    manager.add_city(city4)
    manager.add_city(city5)

    ticket = Ticket(datetime.now(), None)
    ticket.set_flight_date()
    ticket.set_flight_direction(manager)

    available_seat_types = ['Economy', 'Business', 'First']
    seat_type = ticket.select_seat_type(available_seat_types)

    seat_configurations = [
        SeatConfiguration('Economy', 100, 200),
        SeatConfiguration('Business', 50, 400),
        SeatConfiguration('First', 20, 800)
    ]

    distance = manager.calculate_distance(ticket.departure_city, ticket.destination_city)

    total_price = ticket.calculate_cost(seat_configurations, distance)

    ticket.get_flight_info(total_price)
    # directions_from_city1 = manager.list_directions_from_city(ticket.departure_city)
    # for direction in directions_from_city1


if __name__ == "__main__":
    main()