def square_elements(input_list):
    return [x**2 for x in input_list]

def filter_even_numbers(my_list):
    return [x for x in my_list if x % 2 == 0]

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5]
    print(square_elements(input_list))
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_even_numbers(my_list))