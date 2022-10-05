# Main Conception
# hiding info
# encapsulation
# inheritance
# poymorphism

from pyclbr import Function


class Vehicle:
    'this class simulates complex numbers'

    def __init__(self, VIN, weight, manufacturer):
        self.vin_num = VIN
        self.weight = weight
        self.manufacturer = manufacturer

    def GetWeight(self):
        return self.weight

    def GetVin(self):
        return self.vin_num

    def GetManufacturer(self):
        return self.manufacturer

    def VehicleType(self):
        pass

    def SetReal(self, val):
        if (type(val) not in (int, float)):
            raise Exception('Real number input is not a Number')
        self.__real = val

    def SetImag(self, val):
        if (type(val) not in (int, float)):
            raise Exception('Imaginary number input is not a Number')
        self.__imag = val


class Car(Vehicle):
    def __init__(self, VIN, weight, manufacturer, seats):
        self.vin_num = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.seats = seats

    def NumberOfSeats(self):
        return self.seats

    def VehicleType(self):
        return 'CAR'


class Truck(Vehicle):
    def __init__(self, VIN, weight, manufacturer, capacity):
        self.vin_num = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.capacity = capacity

    def TransportCapacity(self):
        return self.capacity

    def VehicleType(self):
        return 'TRUCK'


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
