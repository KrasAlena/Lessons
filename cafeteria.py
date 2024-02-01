#**************************************************************************************
# EXERCISE 2
#
# Cafeteria project : Create a live menu and payment system (a.k.a console program) :
#
# First the program should ask if table was reserved/ not (Providing your full name).
# And then if not would assign you a table (there is a specific number single, double or family tables).
# After table is assigned to you, system should show how many free tables are and
# how which are reserved/occupied. The system must be able to show name/surname of
# the person of the reserved table (CLI option : enter reserved table nuber ;
# OUTCOME: Name/Surname/Time Reserved)
# After assigning table, system should show different menu options for breakfast, lunch,
# dinner , drinks (alcohol. alcohol free), to choose from. Special menu for vegetarian
# and vegan must be included too in the special menu. All menu items should have weight,
# preparation time in minutes, calories, and price.
# I have to have an option to change the order before the payment section.
# Thus I can delete, add more, update amount of the same order.
# I should be able to choose whatever I want from all menus in one ordering.
# After I finish, I need to see what I chosen, the full payable amount and approx
# waiting time for the food to be served
# Add an option to add tips (% from the full cost) to the final bill.
# After the payment , system should generate the receipt (logging).
#**************************************************************************************
import datetime
import logging
logging.basicConfig(level=logging.DEBUG, filename='cafe.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Menu:
    def __init__(self, menu_type: str, items: list):
        self.menu_type = menu_type
        self.items = items

    def display_menu(self):
        print(f'Menu: {self.menu_type}')
        for item in self.items:
            print(f'{item.name} - ${item.price}')


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table:
    def __init__(self, is_occupied: bool, table_type: str, surname: str):
        self._is_occupied = is_occupied
        self._table_type = table_type
        self._surname = surname
        self._reservation_time = None
        self.table_number = 0

    def get_is_occupied(self):
        return self._is_occupied

    def get_table_type(self):
        return self._table_type

    def get_surname(self):
        return self._surname

    def get_reservation_time(self):
        return self._reservation_time

    def set_is_occupied(self, is_occupied):
        self._is_occupied = is_occupied
        if is_occupied:
            self._reservation_time = datetime.datetime.now()
        else:
            self._reservation_time = None

    def set_table_type(self, table_type):
        self._table_type = table_type

    def set_surname(self, surname):
        self._surname = surname

    def set_reservation_time(self, reservation_time):
        self._reservation_time = reservation_time


# class Order():
#     def __init__(self, menu_items, table_number):
#         self.menu_items = menu_items
#         self.table_number = table_number


class Cafeteria:
    def __init__(self, number_single_tables: int, number_double_tables: int, number_family_tables: int):
        self.number_single_tables = number_single_tables
        self.number_double_tables = number_double_tables
        self.number_family_tables = number_family_tables
        self.list_of_tables = []
        pancakes = MenuItem(name='Pancakes', price=8.99)
        salad = MenuItem(name='Salad', price=6.99)
        water = MenuItem(name='Still water', price=1.99)
        wine = MenuItem(name='Red wine', price=5.50)


        menu_breakfast = Menu(menu_type='Breakfast', items=[pancakes, salad])
        menu_drinks = Menu(menu_type='Drinks', items=[water, wine])
        self.menus = [menu_breakfast, menu_drinks]

        self.orders = {}
        table_number = 0

        for i in range(self.number_single_tables):
            table = Table(is_occupied=False, table_type='single', surname='')
            self.list_of_tables.append(table)
            table_number += 1
            table.table_number = table_number

        for i in range(self.number_double_tables):
            table = Table(is_occupied=False, table_type='double', surname='')
            self.list_of_tables.append(table)
            table_number += 1
            table.table_number = table_number

        for i in range(self.number_family_tables):
            table = Table(is_occupied=False, table_type='family', surname='')
            self.list_of_tables.append(table)
            table_number += 1
            table.table_number = table_number

    def display_menu(self, menu_type):
        for menu in self.menus:
            if menu.menu_type == menu_type:
                menu.display_menu()


    def display_table_status(self):
        for i, table in enumerate(self.list_of_tables):
            status = 'Occupied' if table.get_is_occupied() else 'Free'
            print(f'Table {i}: {status}')


    def make_reservation(self, surname: str, table_type: str):
        for table in self.list_of_tables:
            if table.get_table_type() == table_type and table.get_is_occupied() == False:
                table.set_surname(surname)
                table.set_is_occupied(True)
                print(f'Reservation for {table.table_number} table is accepted')
                return table.table_number

        print('Sorry, we don\'t have free tables')

    def check_reservation(self, surname: str):
        for table in self.list_of_tables:
            if table.get_surname() == surname:
                print(f'Table {table.table_number} is reserved for {surname}')
                return table.table_number
        return False

    def make_order(self, table_number, item_name, quantity):
        for i in range(quantity):
            if self.orders.get(table_number) is None:
                self.orders = {table_number: [item_name]}
            else:
                self.orders[table_number].append(item_name)



    def display_menu_names(self):
        print('Menus for today:')
        for menu in self.menus:
            print(menu.menu_type)

    # {'1': ['salad', 'water']}
    def display_bill(self, table_number, tips=0):
        amount = 0
        logging.info(f'Bill for {table_number}: ')
        for item in self.orders[table_number]:
            logging.info(f'Menu item is {item}')
            print(f'Menu item is {item}')
            for menu in self.menus:
                for menu_item in menu.items:
                    if menu_item.name == item:
                        amount += menu_item.price
        amount = amount + (amount / 100 * tips)
        logging.info(f'Total: {amount}')
        print(f'Total: {amount}')



cafe = Cafeteria(3, 5, 4)
customer_surname = input('What is your surname: ')
table_number = cafe.check_reservation(customer_surname)
if table_number:
    print('Please, be sited')
else:
    table_type = input('What kind of table do you prefer: single, double, family? ')
    table_number = cafe.make_reservation(customer_surname, table_type)
cafe.check_reservation(customer_surname)

while True:
    cafe.display_menu_names()
    customer_menu = input('Choose a menu: ')
    if customer_menu == '':
        break
    cafe.display_menu(customer_menu)
    item_to_order = input('Choose an option: ')
    item_quantity = int(input(f'How many {item_to_order} do you want? '))

    cafe.make_order(table_number, item_to_order, item_quantity)
tips = int(input('Enter % of tips: '))
cafe.display_bill(table_number, tips)
