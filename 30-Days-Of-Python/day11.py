# Day 11  - 30DaysOfPython Challenge
import math
import keyword

def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(5,10))

def area_of_circle(radius):
    return math.pi*radius*radius
print(area_of_circle(5))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return('Please only enter numbers!')
        else:
            total += num
    return total 
print(add_all_nums(5,10,15))

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32
print(convert_celsius_to_fahrenheit(30))

def check_season(month):
    if month.lower() in ['september', 'october', 'november']:
        return 'The season is Autumn'
    elif month.lower() in ['december', 'january', 'february']:
        return 'The season is Winter'
    elif month.lower() in ['march', 'april', 'may']:
        return 'The season is Spring'
    elif month.lower() in ['june', 'july', 'august']:
        return 'The season is Summer'
    else:
        return 'Not a valid month'
print(check_season('August'))

def calculate_slope(x1, x2, y1, y2):
    return (y2-y1)/(x2-x1)
print(calculate_slope(5, 3, 2, 5))

def solve_quadratic_eqn(a, b, c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return f'x1 = {x1}, x2 = {x2}'
print(solve_quadratic_eqn(1, 10, 1))

def print_list(arg):
    for item in arg:
        print(item)
print_list(['pizza','chips','ketchup'])

def reverse_list(arr):
    return arr[::-1]
print(reverse_list(['A','B','C']))

def capitalise_list_items(shopping_list):
    return [item.upper() for item in shopping_list]
print(capitalise_list_items(['egg','cheese','milk']))

def add_item(lst, arg):
    return lst + [arg]
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

def remove_item(lst, arg):
    lst.remove(arg)
    return lst
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

def sum_of_numbers(num):
    count = 0
    for i in range(1,num+1):
        count += i
    return count
print(sum_of_numbers(5))

def sum_of_odds(num):
    count = 0
    for i in range(1,num+1,2):
        count += i
    return count
print(sum_of_odds(4))

def sum_of_even(num):
    count = 0
    for i in range(2,num+1,2):
        count += i
    return count
print(sum_of_even(4))

def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in range(1,num+1,2):
        odd_count += 1
    for j in range(2,num+1,2):
        even_count += 1
    return f'{even_count} even numbers and {odd_count} odd numbers'
print(evens_and_odds(100))

def factorial(num):
    count = 1
    for i in range(1,num+1):
        count *= i
    return count
print(factorial(3))

def is_empty(arg):
    if not arg:
        return 'Empty!'
    else:
        return 'Not empty!'
print(is_empty([]))

def calculate_mean(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum/(len(lst))
print(calculate_mean([2, 3, 7, 9]))

def greet(name):
    if not name:
        return 'Hello guest!'
    else:
        return f'Hello {name}'
print(greet(''))
print(greet('Peter'))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
print(is_prime(29)) 
print(is_prime(10)) 

def unique(lst):
    if len(lst) == len(set(lst)):
        return 'Unique'
    else:
        return 'Not unique'
print(unique([2, 3, 3, 4]))
print(unique([2, 3, 4, 5]))

def data_type(lst):
    check = set()
    for item in lst:
        check.add(type(item))
    if len(check) == 1:
        return 'All same data type'
    else:
        return 'Not all same data type'
print(data_type([2,'two']))
print(data_type([2,4]))

def is_valid_variable(name):
    if keyword.iskeyword(name):
        return False

    return name.isidentifier()
print(is_valid_variable("my_variable")) 
print(is_valid_variable("2variable"))
print(is_valid_variable("if"))    
print(is_valid_variable("variable-name"))