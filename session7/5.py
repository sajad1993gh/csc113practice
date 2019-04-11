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
