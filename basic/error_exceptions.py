# Error Handling
# print(5/0)
# try:
#     sum = 0
#     file = open('numbers.txt', "r")
#     for number in file:
#         sum = sum + 1.0/int(number)
#     print(sum)
# except ZeroDivisionError:
#     print("Number in the file is equal to 0")
# except IOError:
#     print("FILE DNE")

# finally:
#     print(sum)
#     file.close()


a = "1"


def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError('This is not String')


try:
    RaiseException(a)
except ValueError as e:
    print(e)

# try:
#     n = int(input("Enter an Integer: "))
# except ValueError:
#     print("That is not an Int")
