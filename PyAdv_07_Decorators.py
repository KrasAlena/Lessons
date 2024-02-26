# **************************************************************************************
# EXERCISE 1
# Write a decorator that decorates a string-returning function in an email style. For
# example: write_email("this is some text") should return
# "To whom it may concern,
# this is some text
# Sincerely,
# Sender"
# **************************************************************************************



def letter_decorator(func: callable):
    def wrapper():
        print('To whom it may concern,')
        func()
        print('Sincerely,\nSender')

    return wrapper


@letter_decorator
def write_email():
    print('Just have a nice day!')


write_email()


# **************************************************************************************
# EXERCISE 2
# Write a decorator debug_mode that makes it clear that some text is for debugging and
# a function print_debug that would be decorated by this. For example, if I call
# print_debug("This should be 0") I would receive "=== DEBUG: This should be 0 ===" in
# the console
# **************************************************************************************
def debug_mode(func: callable):
    def wrapper():
        result = func()
        print(f'=== DEBUG: {result} ===')

    return wrapper


@debug_mode
def print_debug():
    return 'This should be 0'


print_debug()


# **************************************************************************************
# EXERCISE 3
# Write a decorator that decorates a function which only allows to give write numbers
# (int or float). Write some functions which work with numbers and test your implementation
# **************************************************************************************
def number_operations(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError('Arguments must be numeric (int or float)')
        return func(*args)

    return wrapper


@number_operations
def add_numbers(a, b):
    return a + b


@number_operations
def multiplying(a, b, c):
    return a * b * c


adding_result = add_numbers(10, 13.5)
print('Result:', adding_result)

multiplying_result = multiplying(10, 2, 5)
print('Result:', multiplying_result)

try:
    add_numbers(10, '13')
except TypeError as e:
    print('Error:', e)


# **************************************************************************************
# EXERCISE 4
# Write a decorator that "slows down functions" before calling a function. This can be
# useful if many users are trying to connect to your server and you don't want a single
# user to overload your server. Wasting time can be achieved with time.sleep(1)
# **************************************************************************************
import time

def slow_down_decorator(func: callable):
    def wrapper():
        time.sleep(1)
        func()
    return wrapper


@slow_down_decorator
def survey():
    answer = input('Tell us about your experience using our app: ')
    return answer


survey()

# **************************************************************************************
# EXERCISE 5
# Decorate a function such that the function's first argument is necessarily two words.
# For example: greet("Louis Johnson") returns "Hello, Louis Johnson!" but greet("Louis")
# throws an error "to properly greet a person, you need a first and a last name!"
# **************************************************************************************
def name_checking(func):
    def wrapper(text: str):
        if len(text.split()) != 2:
            raise ValueError('To properly greet a person, you need a first and a last name!')
        return func(text)
    return wrapper

@name_checking
def greeting(name: str):
    return f'Hello, {name}!'

result = greeting('Louis Johnson')
print(result)

err = greeting('Louis')
print(err)

import functools
def do_twice(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
    # func(*args, **kwargs)
    # Do something before func
        res = func(*args, **kwargs)
    # Do something after func
        return res
    return wrapper

# **************************************************************************************
# EXERCISE 6
# Write a decorator that limits the number of parameters (say no more than 2 parameters
# for a function)
# **************************************************************************************
import functools
def limit_args(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        if len(args) + len(kwargs) > 2:
            raise ValueError('No more than 2 parameters for a function')
        return func(*args, **kwargs)

    return wrapper


@limit_args
def add_numbers(a, b, c):
    return a + b + c

print(add_numbers(1, 2, 3))

# **************************************************************************************
# EXERCISE 7
# Write a decorator that allows you to pass only string parameters to a function.
# **************************************************************************************
import functools
def only_string(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError('Arguments must be only strings')

        for kwarg, value in kwargs.items():
            if not isinstance(value, str):
                raise TypeError('Arguments must be only strings')

        return func(*args, **kwargs)

    return wrapper


@only_string
def generate_name(name, surname):
    return f'{name} {surname}'


print(generate_name('John', surname='Doe'))
print(generate_name('John', surname=2))

# **************************************************************************************
# EXERCISE 8
# Write a python decorator that would return whether the result of a function is even or
# uneven. Make sure it works for arbitrary inputs. For example, if you decorate the
# following function with this decorator: sum_two_numbers(1, 2)we will get (3, 'odd')
# **************************************************************************************
import functools
def even_or_odd(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError('Arguments must be numeric (int or float)')

        for kwarg, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError('Arguments must be numeric (int or float)')

        if func(*args, **kwargs) % 2 == 0:
            return func(*args, **kwargs), 'Even'
        return func(*args, **kwargs), 'Odd'

    return wrapper

@even_or_odd
def sum_two_numbers(a, b):
    return a + b

@even_or_odd
def multiply(a, b, c):
    return a * b * c


print(sum_two_numbers(1, 2))
print(multiply(1.5, 20, 1))
# **************************************************************************************
# EXERCISE 9
# write a debug decorator that would help you debug function calls. For example, it
# should print out the way the function was called, specifically: take the repr(a) of
# any positional argument to the function,  all{k}={repr(v)} keyword-value pairs from
# keyword arguments. Print out the function name and finally which value the function
# returned. For example, if I have
# @debug
# def make_greeting(name, age=None):
#      if age is None:
#          return f"Howdy {name}!"
#      else:
#          return f"Whoa {name}! {age} already, you're growing up!"
# and then I expect the following output
# >>> make_greeting("Benjamin")
# Calling make_greeting('Benjamin')
# make_greeting() returned 'Howdy Benjamin!'
# 'Howdy Benjamin!'
# **************************************************************************************
import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f'{key}={repr(value)}' for key, value in kwargs.items()]
        parameters = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({parameters})')
        result = func(*args, **kwargs)
        print(f'{func.__name__}() returned {repr(result)}')
        return result

    return wrapper


@debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'

    return f'Whoa {name}! {age} already, you\'re growing up!'


make_greeting('Benjamin')
make_greeting('Benjamin', age=25)

# **************************************************************************************
# EXERCISE 10
# Write a decorator with an argument runs which is the number of times to call the
# function and which prints the average time the decorated function took over the runs
# times. For example long_function() should output "This function took an average of
# 1.23 seconds to run, averaged over 5 runs"
# **************************************************************************************
import functools
import time


def avg_time_runs(runs: int):
    def avg_time(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(runs):
                start_time = time.perf_counter()
                func(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                total_time += run_time

            avg_run_time = total_time / runs
            print(f'This function took an average of {avg_run_time:.4f} seconds to run, averaged over {runs} runs')

        return wrapper

    return avg_time

@avg_time_runs(5)
def long_function():
    # do something
    time.sleep(1)


long_function()

# **************************************************************************************
# EXERCISE 11
# Create 3 decorators for cleaning strings/text. The first decorator should remove
# trailing whitespace in the string. The second decorator should change all spaces into
# underscores. The third decorator should change text into lowercase. Apply all three of
# these decorators to a function which asks input from a user. For example:
# >>> prompt_user()
# >>> John ate an Apple    # this is what the user types in
# >>> john_ate_an_apple
# **************************************************************************************
import functools

def remove_trailing_spaces(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [arg.rstrip() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {key: value.rstrip() if isinstance(value, str) else value for key, value in kwargs.items()}
        return func(*new_args, **new_kwargs)

    return wrapper

def spaces_to_underscores(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [arg.replace(' ', '_') if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {key: value.replace(' ', '_') if isinstance(value, str) else value for key, value in
                      kwargs.items()}
        return func(*new_args, **new_kwargs)

    return wrapper

def text_into_lowercase(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [arg.lower() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {key: value.lower() if isinstance(value, str) else value for key, value in
                      kwargs.items()}
        return func(*new_args, **new_kwargs)

    return wrapper

@remove_trailing_spaces
@text_into_lowercase
@spaces_to_underscores
def prompt_user(text):
    return f'Result is {text}'


result = prompt_user('  John ate an Apple    ')
print(result)
#print(prompt_user('  John ate an Apple    '))