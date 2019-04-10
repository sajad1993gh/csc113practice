
n = int(input("How many?  "))
maxval = float(input("Enter your first?  "))

for i in range(n-1):
    num = float(input("Enter your first?  "))
    if num >= maxval:
        maxval = num

print(maxval)
