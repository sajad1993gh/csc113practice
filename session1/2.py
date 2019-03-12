import math
r_str = input("Enter radius?")
r_int = int(r_str)

circumference= 2 * math.pi * r_int
area = math.pi * (r_int ** 2)
print (circumference, "and", area)
