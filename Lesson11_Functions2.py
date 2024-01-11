#*******************************************
# *args, **kwargs
#*******************************************

def check_arguments(greeting, *args, **kwargs):
    print(greeting)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

check_arguments('welcome', 1, 2, 3, name='Sarah', age=26)

#---------------------------------------------------------------
def print_arguments(a, b, *args, c=5, d=10, **kwargs):
    print(a, b)
    print(args)
    print(c, d)
    print(kwargs)

print_arguments('welcome', 1, 2, 3, name='Sarah', age=26)

#*******************************************
# lambda function
#*******************************************
multiplication = (lambda  x,y :  x * y)(2,3)
print(multiplication)

#**************************************************************************************
# EXERCISE 1
# Write a function that takes two lists and adds the first element in the first list
# with the first element in the second list, the second element in the first list
# with the second element in the second list, etc, etc.
# Return True if all element combinations add up to the same number.
# Otherwise, return False. Example:
#**************************************************************************************
def sum_elements(list1, list2):
    sum_list = map(sum, zip(list1, list2))
    if len(list1) != len(list2):
        return False
    else:
        return len(set(sum_list)) == 1

list1 = [1, 2, 3, 3]
list2 = [4, 3, 2, 2]
print(sum_elements(list1, list2))

#---------------------------------------------------------------
def sum_elements(list1, list2):
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
    if len(list1) != len(list2):
        return False
    else:
        return len(set(sum_list)) == 1

list1 = [1, 2, 3, 1]
list2 = [4, 3, 2, 2]
print(sum_elements(list1, list2))

#**************************************************************************************
# EXERCISE 2
# There's a great war between the even and odd numbers.
# Many numbers already lost their lives in this war and it's your task to end this.
# You have to determine which group sums larger: the evens or the odds. The larger group wins.
# Create a function that takes a list of integers, sums the even and odd numbers separately,
# then returns the difference between the sums of the even and odd numbers.
#**************************************************************************************
def even_odd_war(user_list):
    even_sum = sum([i for i in user_list if i % 2 == 0])
    odd_sum = sum([i for i in user_list if i % 2 != 0])
    return f'{max(even_sum, odd_sum)} - {min(even_sum, odd_sum)} = {max(even_sum, odd_sum) - min(even_sum, odd_sum)}'

user_list = [5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]
print(even_odd_war(user_list))
#---------------------------------------------------------------






#**************************************************************************************
# EXERCISE 3
# You are given an input array of bigrams, and an array of words.
# Write a function that returns True if every single bigram from this array
# can be found at least once in an array of words.
#**************************************************************************************
def if_bigrams_in_list(bigrams, lst):
    all_present = True
    for i in bigrams:
        if i not in ' '.join(lst):
            all_present = False
            break
    return all_present
bigrams = ["ay", "be", "ta", "cu"]
lst = ["beautiful", "the", "hat"]

print(if_bigrams_in_list(bigrams, lst))

#---------------------------------------------------------------
def if_bigrams_in_list(bigrams, lst):
    return all(item in ' '.join(lst) for item in bigrams)

bigrams = ["at", "be", "th", "au", "ay"]
lst = ["beautiful", "the", "hat"]

print(if_bigrams_in_list(bigrams, lst))

#**************************************************************************************
# EXERCISE 4
# Create a function that takes a list of strings and returns a new list
# containing only the strings that start with a vowel.
# Use lambda functions to implement the logic for checking if a string starts with a vowel.
#**************************************************************************************
def starts_with_vowel(lst):
    vowels = 'aeiou'
    return list(filter(lambda x: x[0] in vowels, lst))

lst = ["oo", "mi", "ki", "la"]
print(starts_with_vowel(lst))

#**************************************************************************************
# EXERCISE 5
# Create a lambda function that:
#
# Takes two arguments: a string and a number.
# Returns a new string that repeats the original string as many times as the number.
# For example, if the inputs are Hello and 3, the function should return HelloHelloHello.
#**************************************************************************************
string_multiplication = lambda x, y : x * y
print(string_multiplication('Hello', 3))
