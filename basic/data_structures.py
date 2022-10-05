# Data Structures

# tuple
from ast import Lambda


tup = (1, 'abc', 2, 'cde')
tup1 = 3, 'efg', True

tup2 = 'A'  # tup2 = ('A',)

# prints the full tuple
print(tup)
# prints second element of the tuple
print(tup[1])
# gets a certain portion of the tuple
print(tup[0:2])

# add element to end of tuple
tup = tup[0:3] + (5,)
print(tup)

# return multple results in a tuple


def multiple_results():
    return (1, 2, 'a')


print(multiple_results())

# can compare if tuples are equal to each other
print((1, 2, 'a') == (1, 2))

try:
    tup[3] = 5
except Exception as e:
    print(e)
