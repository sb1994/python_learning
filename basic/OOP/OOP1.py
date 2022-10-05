# Main Conception
# hiding info
# encapsulation
# inheritance
# poymorphism

class Complex:
    'this class simulates complex numbers'

    def __init__(self, real=0, imag=0):
        if (type(real) not in (int, float)) or type(imag) not in (int, float) not in (int, float):
            raise Exception('Parmas are not NUmbers')
        # sets the variables to private
        self.SetReal(real)
        self.SetImag(imag)

    def GetReal(self):
        return self.__real

    def GetImag(self):
        return self.__imag

    def SetReal(self, val):
        if (type(val) not in (int, float)):
            raise Exception('Real number input is not a Number')
        self.__real = val

    def SetImag(self, val):
        if (type(val) not in (int, float)):
            raise Exception('Imaginary number input is not a Number')
        self.__imag = val


# Class instasiation
# yse try/ catch
try:
    #     # c = Complex(1, 1)
    #     c = Complex(1, 1)
    #     print(c.real, c.imag)

    # passing sequences
    c = Complex(2, 3)
    print(c.GetImag(), c.GetReal())
    c.SetImag(2.5)
    print(c.GetImag(), c.GetReal())

except Exception as e:
    print(e)
