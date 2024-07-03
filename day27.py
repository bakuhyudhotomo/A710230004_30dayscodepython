import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN

# Menggunakan round()
print("round(4.6):", round(4.6))
print("round(4.4):", round(4.4))
print("round(4.5678, 2):", round(4.5678, 2))

# Menggunakan math.ceil() dan math.floor()
print("math.ceil(4.2):", math.ceil(4.2))
print("math.ceil(4.7):", math.ceil(4.7))
print("math.floor(4.2):", math.floor(4.2))
print("math.floor(4.7):", math.floor(4.7))

# Menggunakan format string
number = 4.5678
print("Formatted number:", f"{number:.2f}")

# Menggunakan decimal untuk pembulatan
number = Decimal('4.675')
rounded_up = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
rounded_down = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_DOWN)
print("Decimal ROUND_HALF_UP:", rounded_up)
print("Decimal ROUND_HALF_DOWN:", rounded_down)