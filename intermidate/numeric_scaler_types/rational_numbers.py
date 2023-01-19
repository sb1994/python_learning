# imports
from fractions import Fraction
from decimal import Decimal

two_thirds = Fraction(2, 3)
print('Two Thirds {}'.format(two_thirds))
four_fifths = Fraction(4, 5)
print('Four Fifths {}'.format(four_fifths))


# can use decimal to refine the number and get the correct number
float_fraction = Fraction(Decimal('0.1'))
print('Float Fractions {}'.format(float_fraction))
