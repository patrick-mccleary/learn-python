# Day 4 - 30DaysOfPython Challenge

# Exercise 1

broken = ['Thirty', 'Days', 'Of', 'Python']
joined = ' '.join(broken)
print(joined)

# Exercise 2

broken2 = ['Coding', 'For', 'All']
joined2 = ' '.join(broken2)
print(joined2)

# Exercise 3

company = "Coding For All"

# Exercise 4

print(company)

# Exercise 5

print(len(company))

# Exercise 6

print(company.upper())

# Exercise 7

lower = company.lower()
print(lower)

# Exercise 8

title = lower.title()
print(title)

# Exercise 9

first_word = company.split()[0]
print(first_word)

# Exercise 10

if 'Coding' in company:
    print("Yes, 'Coding' is found in the string.")

# Exercise 11

python_for_all = company.replace('Coding', 'Python')
print(python_for_all)

# Exercise 12

print(python_for_all.replace('All', 'Everyone'))

# Exercise 13

print(company.split())

# Exercise 14

big_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_companies.split(', '))

# Exercise 15

character1 = company[0]
print(character1)

# Exercise 16

last_character = company[-1]
print(last_character)

# Exercise 17

character10 = company[9]
print(character10)

# Exercise 18

phrase = 'Python For Everyone'
acronym1 = ''.join(word[0].upper() for word in phrase.split())
print(acronym1)

# Exercise 19

acronym2 = ''.join(word[0].upper() for word in company.split())
print(acronym2)

# Exercise 20

print(company.index('C'))

# Exercise 21

print(company.index('F'))

# Exercise 22

snippet = 'Coding For All People'
print(snippet.rfind('l'))

# Exercise 23

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# Exercise 24

print(sentence.rfind('because'))

# Exercise 25

extract = 'because because because'
start = sentence.find(extract)
end = start + len(extract)
sliced = sentence[start:end]
print(sliced)

# Exercise 26

print(sentence.find('because'))

# Exercise 27

print(sliced)

# Exercise 28

print(company.startswith('Coding'))     

# Exercise 29

print(company.endswith('coding'))

# Exercise 30

bloated = '   Coding For All      ' 
print(bloated.strip())

# Exercise 31

answer = 'thirty_days_of_python'
print(answer.isidentifier())

# Exercise 32

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# Exercise 33

print("I am enjoying this challenge.\nI just wonder what is next.")

# Exercise 34

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Exercise 35

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} metres square.")

# Exercise 36

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")