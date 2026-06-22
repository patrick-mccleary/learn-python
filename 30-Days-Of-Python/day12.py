# Day 12  - 30DaysOfPython Challenge

from random import randint, choices, choice, shuffle
from string import ascii_letters

def random_user_id(length):
    id = []
    alphabet = []
    for letter in ascii_letters:
        alphabet.append(letter)
    for num in range(length):
        if randint(0, 1) == 0:
            id.append(str(randint(0,9)))
        else:
            id.append(alphabet[randint(0, len(alphabet) - 1)])
    return ''.join(id)

def user_id_gen_by_user():
    length = int(input('Enter desired length: '))
    quantity = int(input('Enter how many you want to generate: '))
    for i in range(quantity):
        print(random_user_id(length))
user_id_gen_by_user()

def rgb_color_gen():
    return f'rgb({randint(0,255)}, {randint(0,255)}, {randint(0,255)})'
print(rgb_color_gen())

def list_of_hexa_colors(n):
    hex_chars = '0123456789abcdef'
    colors = []
    for i in range(n):
        color = '#' + ''.join(choices(hex_chars, k=6))
        colors.append(color)
    return colors
print(list_of_hexa_colors(7))

def list_of_rgb_colors(n):
    rgbs = []
    for i in range(n):
        rgbs.append(rgb_color_gen())
    return rgbs
print(list_of_rgb_colors(5))

def generate_colors(format: str, num: int):
    if format == 'hexa':
        return list_of_hexa_colors(num)
    elif format == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return 'Please enter either hexa or rgb!'
print(generate_colors('rgb', 7))

def shuffle_list(lst: list):
    shuffle(lst)
    return lst
print(shuffle_list([1,2,3,4,5,6]))

def seven_random_nums():
    lst = []
    possible = [0,1,2,3,4,5,6,7,8,9]
    for i in range(7):
        rand = choice(possible)
        possible.remove(rand)
        lst.append(rand)
    return lst
print(seven_random_nums())

