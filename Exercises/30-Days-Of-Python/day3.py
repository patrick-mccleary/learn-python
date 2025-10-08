age = 22
height = 177.8
complex_number = 3 + 2j

base = float(input('Enter base: '))
height = float(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is: ', area)

a = input('Enter length of side a: ')
b = input('Enter length of side b: ')
c = input('Enter length of side c: ')
perimeter = a + b + c
print('The perimeter of the triangle is: ', perimeter)

length = int(input('Enter length of rectangle: '))
width = int(input('Enter width of rectangle: '))
area = length * width
print('The area of the rectangle is: ', area)

import math
radius = float(input("Enter radius of the circle: "))
pi = 3.14
circle_area = pi * radius ** 2
circumference = 2 * pi * radius
print("Area of the circle:", circle_area)
print("Circumference of the circle:", circumference)

slope = 2
y_intercept = -2
x_intercept = y_intercept / -slope  # Set y=0, solve for x
print("Slope:", slope)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Slope between points:", slope_points)
print("Euclidean distance:", distance)

print("Slope from y=2x-2:", slope)
print("Slope between points:", slope_points)
if slope == slope_points:
    print("The slopes are equal.")
else:
    print("The slopes are different.")

for x in range(-10, 11):
    y = x ** 2 + 6 * x + 9
    print(f"x={x}, y={y}")
    if y == 0:
        print(f"y is zero when x = {x}")

length_python = len('python')
length_dragon = len('dragon')
print(length_python != length_dragon)

print('on' in 'python' and 'on' in 'dragon')

sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

print('on' not in 'dragon' and 'on' not in 'python')

text = 'python'
length = len(text)
length_float = float(length)
length_str = str(length_float)
print(length)
print(length_float)
print(length_str)

number = int(input("Enter a number to check if it is even: "))
print(number % 2 == 0)

print(7 // 3 == int(2.7))

print(type('10') == type(10))

try:
    print(int('9.8') == 10)
except ValueError:
    print("Cannot convert '9.8' to int directly.")

hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print(pay)

seconds_left = (100 - age) * 365 * 24 * 3600
print('You have this many seconds left: ', seconds_left)

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")