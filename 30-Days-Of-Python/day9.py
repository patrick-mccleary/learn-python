# Day 9 - 30DaysOfPython Challenge

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    remain = 18 - age
    print(f'You need {remain} more years to learn to drive.')

my_age = 23
your_age = int(input('Please enter your age: '))
if my_age > your_age:
    if my_age - your_age == 1:
        print(f'You are 1 year younger than me')
    else:
        print(f'You are {my_age - your_age} years younger than me')
elif your_age > my_age:
    if your_age - my_age == 1:
        print(f'You are 1 year older than me')
    else:
        print(f'You are {your_age - my_age} years older than me')
else:
    print('We are the same age')

n1 = int(input('Enter number one: '))
n2 = int(input('Enter number two: '))
if n1 > n2:
    print(f'{n1} is greater than {n2}')
elif n2 > n1:
    print(f'{n1} is smaller than {n2}')
else:
    print(f'{n1} is equal to {n2}')


grade = int(input('Enter your grade: '))
if 89 < grade:
    print(f'You achieved a grade A')
elif 79 < grade < 90:
    print(f'You achieved a grade B')
elif 69 < grade < 80:
    print(f'You achieved a grade C')
elif 59 < grade < 70:
    print(f'You achieved a grade D')
else:
    print(f'You achieved a grade F')

month = input('Enter the month: ')
if month.lower() in ['september', 'october', 'november']:
    print('The season is Autumn')
elif month.lower() in ['december', 'january', 'february']:
    print('The season is Winter')
elif month.lower() in ['march', 'april', 'may']:
    print('The season is Spring')
elif month.lower() in ['June', 'July', 'August']:
    print('The season is Summer')
else:
    print('Not a valid month')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter the fruit: ')
if fruit.lower() in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

skills = person['skills']
if 'skills' in person:
    if 'Python' in skills:
        print(skills)
    else:
        print(skills[len(skills)//2])

if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')

if person['is_married'] and 'Finland' in person['country']:
    first = person['first_name']
    last = person['last_name']
    print(f'{first} {last} lives in Finland. He is married.')