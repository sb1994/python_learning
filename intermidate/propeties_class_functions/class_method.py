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
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial())
