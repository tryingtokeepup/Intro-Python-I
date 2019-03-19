"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

renderedCalendar = calendar.TextCalendar()


if len(sys.argv) == 1:
    # cast it to string? i dunno.
    month = datetime.now().month
    month_str = datetime.now().strftime('%B')
    year = datetime.now().year
    print(f'The month is {month_str} and the year is: {year}')
    # don't forget the order! year first, month next when rendering!
    renderedCalendar.prmonth(int(year), int(month))
elif len(sys.argv) == 2:
    month = sys.argv[1]
    year = datetime.now().year

    print(
        f"I'm going to assume you entered today's month! \n The month is : {sys.argv[1]}. The year is {year}. \n Now, check out the calandar!")
    renderedCalendar.prmonth(int(year), int(month))


elif len(sys.argv) == 3:
    month = sys.argv[1]
    year = sys.argv[2]
    print(
        f"Great job! I'm going to render the {sys.argv[1]} month and year {sys.argv[2]}")
    renderedCalendar.prmonth(int(year), int(month))

else:
    print("Invalid command:")
