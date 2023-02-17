"""
Write a Python program to subtract five days from current date.
"""
import datetime
from datetime import date, timedelta

print(date.today() - timedelta(5))

Five_days_ago = datetime.date.today() - datetime.timedelta(days=5)

print(Five_days_ago)

print(datetime.date.today().strftime("%A"))

print(Five_days_ago.strftime("%A"))
