import math
import datetime

r_str = input("Enter radius?\n")
r_int = int(r_str)

circumference= 2 * math.pi * r_int
area = math.pi * (r_int ** 2)
print (circumference, "and", area)


now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S\n"))
