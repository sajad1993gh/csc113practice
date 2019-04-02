
# interactive loop
sum = 0
count = 0
moredata = "yes"
while moredata[0] == "y" or moredata[0] == "Y":
    x = float(input("Enter number>> "))
    sum = sum + x
    count = count + 1
    moredata = input("more ? >> ")
print("\n", sum/count)


# sentinel loops

xStr = input("Enter number>> ")
sum = 0;
count = 0;
while xStr != "":
    x = float(xStr)
    sum = sum + x
    count = count + 1
    xStr = input("more ? >> ")
print("\n", sum/count)


# Nested loops:
print("NESTED LOOPS:\n")
for i in range(10):
   for i in range(10):
       print(i*i)  # handle the inner loop first

print("NESTED LOOPS:\n")
for i in range(10):
   for i in range(10):
       print(i)

print("NESTED LOOPS:\n")
for i in range(1, 5+1):

   for j in range(1, i+1):
       print("*", end=" ")

   print()

   """
*
* *
* * *
* * * *
* * * * *

"""
