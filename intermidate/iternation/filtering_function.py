numbers = [-2, -1, 0, 1, 2]

# uses the lambda function to to filter out the negative numbers
positive_numbers = filter(lambda n: n > 0, numbers)

list(positive_numbers)


def is_positive(n):
    return n > 0


print(list(filter(is_positive, numbers)))
