print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# will return true

print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# will return false

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# function
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
# function return 0, that is == to false

def myFunction() :
  return True

print(myFunction())

# exited true

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# another example

x = 200
print(isinstance(x, int))

# will show true
