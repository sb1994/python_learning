# math module cannot be used with complex number so cmath must be used
import cmath

print(2j)
# displays the real and imaginary parts
print(3+4j)

# complex constructor can also be used
c = complex(3)

# to extract the real and imaginary use
print('The real number is {}'.format(c.real))
print('The imaginary number is {}'.format(c.imag))

# print the sqrt of a complex number
print('Sqrt {}'.format(cmath.sqrt(-1)))

# to get the phase of a cnum
print('Sqrt Phase {}'.format(cmath.phase(1+1j)))
