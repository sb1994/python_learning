from ast import If


def factorial(n):
    if n == 1:
        return 1

    else:
        return n*factorial(n-1)


print(factorial(5))


def tail_recursion(n, accumulator=0):
    if n == 0:
        return accumulator

    else:
        return tail_sum(n-1, accumulator+n)


print(tail_recursion(10))
