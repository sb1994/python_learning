# functions

from unittest import result


def function():
    print('This is the first funtions')


function()

# return value to a function


def returning():
    return "I am a result that was returned from a function"


result = returning()
print(result)

# returning multiple values


def multival():
    return "this is a result", 2


print(multival())
