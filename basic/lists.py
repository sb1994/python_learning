from tabnanny import check


list1 = [1, 'abe', (2, 3)]
print(list1[2][0])

# can add element to the end of the tup
# print(list1+['4'])

# make a copy of the list and add it to the end
# print(list1*2)

# check if element exists in tuple
print(list1 == [1, 'abe', (2, 3)])

# list functions
print(list(map(lambda x: x**2+3*x+1, [1, 2, 3, 4])))

# filter
print(filter(lambda x: x < 4, [1, 2, 3, 4, 5, 4, 3, 2, 1]))
