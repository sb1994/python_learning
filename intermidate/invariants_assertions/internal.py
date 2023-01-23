def modulus_3(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:
        assert r == 2, "Remainder is not 2"
        print("Remainder 2")


def modulus_4(n):
    r = n % 4
    if r == 0:
        print("Multiple of 4")
    elif r == 1:
        print("Remainder 1")
    else:
        assert r == 3, "Remainder is not 3"
        print("Remainder 3")
