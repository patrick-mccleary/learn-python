# Day 8 - 30DaysOfPython Challenge

dog = {}

dog['name'] = 'Clifford'
dog['color'] = 'Red'
dog['legs'] = 4
dog['age'] = 2
print(dog.items())

student = {
    'first_name':'Patrick',
    'last_name':'McCleary',
    'gender':'Male',
    'age':23,
    'marital':'Single',
    'skills':['coding','problem-solving'],
    'country':'UK',
    'city':'Leeds',
    'address':'The Granary'
}
print(student.items())

print(len(student))

print(student['skills'])
print(type(student['skills']))

student['skills'] = ['coding','problem-solving','leadership','critical thinking']
print(student['skills'])

print(student.keys())

print(student.values())

student_tp = student.items()
print(student_tp)

del student['address']
print(student.keys())

del student

