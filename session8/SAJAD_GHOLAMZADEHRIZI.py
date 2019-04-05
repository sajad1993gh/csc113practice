# SAJAD_GHOLAMZADEHRIZI
# SESSION AFTERNOON 1 _ Assignment 4
import math

def perf_int(n):
    try:
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n
    except ValueError:
        print("Please enter valid integers")
    except:
        print("\nSomething went wrong, sorry!")

x = int(input("Enter an integer to check if it's perfect? \n"))
n = perf_int(x)
if str(n) == "True":
    print("Yes it is perfect")
else:
    print("No it's not perfect")

z = int(input("Enter a positive integer to get the divisors:\n"))
print("The divisors are:")
for i in range(1, z+1):
    if(z % i == 0):
        print(i)

def is_triangle(a, b, c):
    n = (b - c)
    if n < 0 :
        n = -n
    if n < a :
        if a < b + c:
            return True
    return False

def get_vertex():
    x = float(input("    Please enter x: "))
    y = float(input("    Please enter y: "))
    return x,y

def get_triangle():
    print("First vertex")
    x1,y1 = get_vertex()
    print("Second vertex")
    x2,y2 = get_vertex()
    print("Third vertex")
    x3,y3 = get_vertex()
    return x1, y1, x2, y2, x3, y3

x1, y1, x2, y2, x3, y3 = get_triangle()

a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
b = math.sqrt((x3-x1)**2 + (y3-y1)**2)
c = math.sqrt((x3-x2)**2 + (y3-y2)**2)

if is_triangle(a, b, c):
    print("Yes they form a triangle")
else:
    print("No they can't form a triangle")


first = int(input("Enter an integer to start from:\n"))
last = int(input("Enter an  integer to end:\n"))

def is_prime(i):
    isPrimeBool = True
    if n < 2:
        isPrimeBool = False
    else:
        for i in range(2,n):
            if n % i == 0:
                isPrimeBool = False
    return isPrimeBool

for i in range(first,last + 1):
    if is_prime(i):
        print(i)
