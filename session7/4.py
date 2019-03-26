
# interactive loop
sum = 0
count = 0
moredata = "yes"
while moredata[0] == "y":
    x = float(input("Enter number>> "))
    sum = sum + x
    count = count + 1
    moredata = input("more ? >> ")
print("\n", sum/count)
