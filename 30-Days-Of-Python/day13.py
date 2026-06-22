# Day 13  - 30DaysOfPython Challenge

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [i for i in numbers if i > 0 ]
print(filtered)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [i for i in list_of_lists for i in i]
print(flattened)

tup = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(tup)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [
    [country.upper(), country[:3].upper(), city.upper()] 
    for sublist in countries 
    for country, city in sublist
]
print(output)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [
    {'country': country.upper(), 'city': city.upper()} 
    for sublist in countries 
    for country, city in sublist
]
print(output)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [
    f'{first} {last}'
    for sublist in names
    for first, last in sublist
]
print(output)

slope_calculator = lambda x1, y1, x2, y2: (
    (y2 - y1) / (x2 - x1)
)
print(slope_calculator(4,2,3,4))