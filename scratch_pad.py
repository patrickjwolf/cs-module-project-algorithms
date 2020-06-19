"""
I want to be able to print the area of a circle,
Ideally, I want to print only the third decimal
place.
"""
import math
radius = 3

print(round(math.pi * radius * radius), 3)
print(f"The area of the circle is {math.pi * radius * radius:.3f}")