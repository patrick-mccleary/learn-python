# Day 6 - 30DaysOfPython Challenge

empty_tpl = ()

sisters = ('Molly', 'Caitlin')
brothers = ('Jonny', 'Tom')
siblings = sisters + brothers

print(len(siblings))

parents = ('Sue', 'Brian')
family = siblings + parents
print(family)
*siblingss, mum, dad = family
print(siblingss)
print(mum)
print(dad)

fruits = ('apple', 'mango', 'pear')
vegetables = ('carrot', 'pepper', 'broccoli')
animal_products = ('beef', 'chicken', 'pork')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_index = len(food_stuff_lt)//2
del food_stuff_lt[middle_index]
print(food_stuff_lt)

del food_stuff_lt[:3]
del food_stuff_lt[-3:]
print(food_stuff_lt)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('YES')
else:
    print('NO')

if 'Iceland' in nordic_countries:
    print('YES')
else:
    print('NO')