
# **************************************************************************************
# EXERCISE 1
# Write a Python script that reads a CSV file containing sales data (date, product,
# quantity, price) and prints out only the rows where the quantity sold is greater than 10.
# **************************************************************************************
import csv

with open('sales.csv', newline='') as csvfile:
    sales_data = csv.reader(csvfile)
    next(sales_data)

    for row in sales_data:
        if int(row[2]) >= 20:
            print(row)


# **************************************************************************************
# EXERCISE 2
# Write a Python script that reads a CSV file containing employee information (name,
# salary) and increases the salary of each employee by 10%. Then, write the updated
# information back to the same CSV file.
# **************************************************************************************
import csv

with open('stuff.csv', 'r', newline='') as file:
    data = csv.reader(file)
    header = next(data)

    updated_rows = []

    for row in data:
        name, salary = row
        updated_salary = str(round((float(salary) * 1.10), 2))
        updated_rows.append([name, updated_salary])

with open('stuff.csv', 'w', newline='') as file:
    new_data = csv.writer(file)
    new_data.writerow(header)
    new_data.writerows(updated_rows)


# **************************************************************************************
# EXERCISE 3
# Given two CSV files containing student information (name, age, grade) and (name, year
# of study), write a Python script that merges the two files based on the student's name
# and prints out the combined information.
# **************************************************************************************
import csv

with open('csv_students.csv', newline='') as csvfile1, open('students_info.csv', newline='') as csvfile2:
    students_data = csv.reader(csvfile1)
    students = csv.reader(csvfile2)
    next(students_data)
    next(students)

    merged_info = []

    for student_data in students_data:
        name, age, grade = student_data

        for student_info in students:
            if student_info[0] == name:
                year_of_study = student_info[1]
                merged_info.append([name, age, grade, year_of_study])
                break
        else:
            merged_info.append((name, age, grade, 'N/A'))

for info in merged_info:
    print(info)

# **************************************************************************************
# EXERCISE 4
# Write a Python script that reads a CSV file containing student information (name, age,
# grade) where some rows may have missing data. Handle these missing values gracefully,
# such as by replacing them with a default value or skipping those rows.
# **************************************************************************************
import csv

with open('students4task.csv', 'r', newline='') as file:
    data = csv.reader(file)
    header = next(data)
    cleaned_data = []
    for row in data:
        cleaned_row = [item if item else 'N/A' for item in row]
        cleaned_data.append(cleaned_row)

with open('students4task.csv', 'w', newline='') as file:
    new_data = csv.writer(file)
    new_data.writerow(header)
    new_data.writerows(cleaned_data)

# **************************************************************************************
# EXERCISE 5
# Write a Python script that reads a CSV file containing student information and validates
# each row to ensure that the age is a positive integer and the grade is a valid letter
# grade (A, B, C, D, or F). Print out any rows that fail the validation check.
# **************************************************************************************
import csv

with open('csv_students.csv', 'r', newline='') as file:
    data = csv.reader(file)
    next(data)

    grades = ['A', 'B', 'C', 'D', 'F']
    for row in data:
        name, age, grade = row
        if not (age.isdigit() and int(age) > 0 and grade in grades):
            print(f'Validation failed for the row: {row}')



# **************************************************************************************
# EXERCISE 6
# Write a Python script that reads a CSV file containing sales data and calculates the
# total revenue generated by each product. Then, write the results to a new CSV file
# with columns for product name and total revenue.
# **************************************************************************************
import csv

products_revenue = {}

with open('csv_sales_data.csv', 'r', newline='') as file:
    data = csv.reader(file)
    next(data)

    for product_data in data:
        product, quantity, price = product_data
        total_revenue = int(quantity) * float(price)

        if product in products_revenue:
            products_revenue[product] += total_revenue
        else:
            products_revenue[product] = total_revenue


with open('product_revenue.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product', 'Total Revenue'])

    for product, revenue in products_revenue.items():
        writer.writerow([product, revenue])


#=============================JSON TASKS=========================================

'''Exercise 6: Convert the following Vehicle Object into JSON
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Convert it into JSON format

Output (json):
{
    "name": "Toyota Rav4",
    "engine": "2.5L",
    "price": 32000
}
'''
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

    def write_to_json(self):
        with open('vehicles.json', 'a') as file:
            vehicle_info = {
                'Name': self.name,
                'Engine': self.engine,
                'Price': self.price
                }
            file.write(json.dumps(vehicle_info) + '\n')

    def convert_to_json(self):
        print(json.dumps(self.__dict__, indent=4))


vehicle = Vehicle('Toyota Rav4', '2.5L', 32000)
#vehicle.write_to_json()
vehicle.convert_to_json()


vehicle2 = Vehicle('Porsche 911', '3.5L', 332000)
vehicle2.write_to_json()
vehicle2.convert_to_json()

'''
Exercise 7: Convert the following JSON into Vehicle Object
{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }

For example, we should be able to access Vehicle Object using the dot operator like this.
vehicleObj.name, vehicleObj.engine, vehicleObj.price
'''
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicles = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

vehicle_dict = json.loads(vehicles)
vehicleObj = Vehicle(vehicle_dict['name'], vehicle_dict['engine'], vehicle_dict['price'])



print(vehicleObj.name)