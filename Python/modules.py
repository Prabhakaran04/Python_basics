import datetime
import math
import calendar

# datetime
current_time = datetime.datetime.now()
date1 = datetime.date(2003, 3, 14)
time1 = datetime.time(12, 12, 12)
print('Your current system time is', current_time)
print('The date object created is', date1)
print('The time object created is', time1)
print('The combined date time is', datetime.datetime.combine(date1, time1))

# math
print('The ceiling value of your input is', math.ceil(10.86))
print('The floor value of your input is', math.floor(10.86))
print('The square root of your input is', math.sqrt(34))
print('The factorial of your input is', math.factorial(89))
print('The powered output of your input is', math.pow(3, 2))
print('The combination that can be made in your given inputs are', math.comb(5, 1))

# calendar
print('provides list of days of week', list(calendar.day_name))
print('provides list of mons of yr in short form', list(calendar.month_abbr))
print('provides tha calendar of 2002', calendar.calendar(2002))
print('says that a given year is leap yr or not', calendar.isleap(2020))
print('displays the whole mon of the given input',
      calendar.monthcalendar(2002, 3))
print('displays which day is the given input', calendar.weekday(2003, 3, 14))
print('provides the days of week name header', calendar.weekheader(5))
