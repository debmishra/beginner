import calendar
import datetime
import time

print(calendar.weekheader(3))
print()
print(calendar.firstweekday())
print()
print(calendar.month(2019,3))
print()
print(calendar.monthcalendar(2019,3))
# print()
# print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020, 3, 8)
print()
print (day_of_the_week)

is_leap = calendar.isleap(2100)
print()
print (is_leap)
print()
print(calendar.leapdays(2000, 2105))