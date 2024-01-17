class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f'Student ID: {self.student_id}')
        print(f'Name: {self.name}')
        print(f'Grade: {self.grade}')
        if hasattr(self, 'major'):
            print(f'Major: {self.major}')
        else:
            print('Major: Computer Science')

    def promote(self):
        if self.grade < 12:
            self.grade += 1
            print(f'{self.name} has been promoted to grade {self.grade}')
        else:
            print(f'{self.name} has already completed their studies!')

# Example usage:
student1 = Student(student_id=1, name='John Doe', grade=10)
student1.major = 'Law'
student1.display_info()
student1.promote()

student2 = Student(student_id=2, name='Jane Smith', grade=12)
student2.display_info()
student2.promote()

#__________________________________________________________________________-
class Account:

    def __init__(self, amount=0):
        self.amount = amount

    def receive_money(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            print(f"withdrawn {amount}, {self.amount} remaining")
        else:
            print("not enough money")


account1 = Account()

account2 = Account(2000)

account1.withdraw(10)

account1.receive_money(5000)

account1.withdraw(10)

account2.withdraw(50)