my_set = set(['one', 'two', 'three', 'one'])
my_set1 = set(['two', 'three', 'four'])
# duplicate are removed
# print(my_set)

# union
# |
print(my_set | my_set1)
# interesection
# ^ returns only unique values
print(my_set ^ my_set1)

# set functions
print(set.union(my_set, my_set1))
print(set.intersection(my_set, my_set1))
print(set.difference(my_set1, my_set))
