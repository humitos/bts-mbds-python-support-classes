# -*- coding: utf-8 -*-

import datetime
import sys
import time


print('Welcome to Simple Alarm!')
print('Please enter the date and time where you want to be notified')
print('Following the format MM/DD/YY HH:MM')
date_input = input()

print('Please enter the description for this reminder')
description_input = input()


try:
    date_format = '%m/%d/%y %H:%M'
    date = datetime.datetime.strptime(date_input, date_format)
except ValueError:
    print('The date is in an incorrect format')
    print('Exiting...')
    sys.exit(1)

print(f'Thanks. I will remind you about "{description_input}" at {date}.')

while True:
    if datetime.datetime.now() > date:
        print(f'Hey remember to do: {description_input}')
        break

    time.sleep(30)

print('Good bye.')
