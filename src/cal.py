# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
#
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.

import sys
import calendar
import datetime

# month = int(input("Enter a month: "))
# year = int(input("Enter a year: "))
calendar.setfirstweekday(6)

if len(sys.argv) != 3:
  month = sys.argv[1]
  year = sys.argv[2]
  print(calendar.month(int(year), int(month)))
else:
  month = datetime.date.today().month
  year = datetime.date.today().year
  print(calendar.month(year, month))