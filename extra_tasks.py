import random
comp_choice = random.choice(['R', 'S', 'P'])

user_choice = input('Make a choice from R, P or S: ')

print(f'Computer choice - {comp_choice}')
if user_choice == comp_choice:
    print('Draw')
elif (user_choice == 'R' and comp_choice == 'S') or (user_choice == 'P' and comp_choice == 'R') or (user_choice == 'S' and comp_choice == 'P'):
    print('User wins!')
else:
    print('Computer wins!')



input_year = int(input("input a year "))
if input_year % 4 == 0:
    if input_year % 100 != 0:
        print("leap year")
    else:
        if input_year % 400 == 0:
            print ("leap year")
        else:
            print("not a leap year")
else:
    print("not a leap year")

#ready to push