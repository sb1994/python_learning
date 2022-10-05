my_dic = {'Key': 'Value', 'name': 'S B'}

my_dic1 = {x: x+1 for x in range(10)}
print(my_dic)
print(my_dic1)


# print(my_dic.keys())
# print(my_dic.values())

my_dic[1] = 2
print(my_dic)

# delete key from dic
del my_dic[1]
print(my_dic)

# empty the dic
my_dic.clear()
print(my_dic)
