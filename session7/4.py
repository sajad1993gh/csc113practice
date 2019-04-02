
# interactive loop
sum = 0
count = 0
moredata = "yes"
while moredata[0] == "y" | moredata[0] == "Y":
    x = float(input("Enter number>> "))
    sum = sum + x
    count = count + 1
    moredata = input("more ? >> ")
print("\n", sum/count)


# sentinel loops

xStr = input("Enter number>> ")

while xStr != "":
    x = float(xStr)
    sum = sum + x
    count = count + 1
    moredata = input("more ? >> ")
print("\n", sum/count)


# Nested loops:
for i in range(10):
    for i in range(10):
        print(i*i)  # handle the inner loop first
