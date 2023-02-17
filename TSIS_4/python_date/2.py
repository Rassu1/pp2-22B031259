"""
Write a Python program to print yesterday, today, tomorrow.
"""

import datetime

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)

tomorrow = today + datetime.timedelta(days=1)
print('Yesterday : ', yesterday, yesterday.strftime("%A"))
print('Today : ', today, today.strftime("%A"))
print('Tomorrow : ', tomorrow, tomorrow.strftime("%A"))
