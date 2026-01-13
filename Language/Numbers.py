1, 23, 3493                    # Decimal integer literals
0b010101, 0b110010, 0B01       # Binary integer literals
0o1, 0o27, 0o6645, 0O777       # Octal integer literals
0x1, 0x17, 0xDA5, 0xda5, 0Xff  # Hexadecimal integer literals
111_111, 1_111, 11111_1, 11_11_11 # Underscores as visual separators, have no meaning to the interpreter
0., 0.0, .0, 1., 1.0, 1e0, 1.e0, 1.0E0  # Floating-point literals

2.5.as_integer_ratio() # result: tuple (5, 2)

2.5.is_integer() # returns False

##############
# Decimal and Fraction types
##############

from decimal import Decimal
from fractions import Fraction

third_fraction = Fraction(1, 3)
third_fixed = Decimal("0.333")
third_float = 1 / 3

print(third_fraction)  # 1/3
print(third_fixed)     # 0.333
print(third_float)     # 0.3333333333333333

third_float = float(third_fraction)
print(third_float)     # 0.3333333333333333

third_float = float(third_fixed)
print(third_float)     # 0.333