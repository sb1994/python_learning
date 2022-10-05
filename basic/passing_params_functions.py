# Functions

from unittest import result


def add(a, b):
    c = a+b
    return c


result = add(4, 5)

print(result)

# set the default parameter


def default_param(a, b=4, c=5):
    return a + b + c


result = default_param(3)
print(result)
