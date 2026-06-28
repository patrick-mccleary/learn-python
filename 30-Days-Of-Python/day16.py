# Day 16  - 30DaysOfPython Challenge

from datetime import date, datetime

today = datetime.today()
ts = datetime.timestamp(today)

print(today.day)
print(today.month)
print(today.year)
print(today.hour)
print(today.minute)
print(ts)

format = today.strftime('%m/%d/%Y, %H:%M:%S')
print(format)

date_string = '5 December, 2019'
date_object = datetime.strptime(date_string, "%d %B, %Y")

print(date_object)

today = date(year=today.year,month=today.month,day=today.day)
new_year = date(year=2026,month=1,day=1)
diff = today - new_year
print(diff)

print(f'{ts} seconds')