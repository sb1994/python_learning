from iso6346 import create


class ShippingContainer:
    next_serial = 1337

    # creates an internationaly recegnized serial code
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return create(owner_code=owner_code, serial=(str(serial).zfill(6)))

    # create classmethods
    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    # can be used to create an empty class object
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())


class RefrigeratedShippingContainer(ShippingContainer):

    # make a per container temp attribute
    MAX_CELSIUS = 4.0

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(farenheit):
        return (farenheit - 32) * 5 / 9

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp is Too Hott!!")
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temp is Too Hott!!")
        self.celsius = value

    @property
    def farenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @farenheit.setter
    def farenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)
