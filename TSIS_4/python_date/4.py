"""
Write a Python program to calculate two date difference in seconds.
"""
import datetime
import random

rnd = random.randrange(1, 365)

print(rnd)

dt_one = datetime.datetime.now()
dt_two = datetime.datetime.now() - datetime.timedelta(days=rnd)
print(dt_one)
print(dt_two)
print((dt_one-dt_two).days * 24 * 3600 + (dt_one-dt_two).seconds)
