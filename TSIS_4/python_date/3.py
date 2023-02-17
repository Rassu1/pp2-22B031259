"""
Write a Python program to drop microseconds from datetime.
"""

import datetime

x = datetime.datetime.now()

y = x - datetime.timedelta(microseconds=1)

print(x.strftime("%f"))
print(y.strftime("%f"))