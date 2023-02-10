import json

x = { "DN":"John", "SPEED": "inherit", "MTU":"9150"}

# parse x:
y = json.dumps(x)

# the result is a Python dictionary:
print(y)
