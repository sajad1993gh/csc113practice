# SAJAD_GHOLAMZADEHRIZI
# SESSION AFTERNOON 1 _ Assignment 4
import math
# 1

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

# 2

z = int(input("Enter a positive integer to get all positive integer divisors:\n"))
print("The divisors are:")
for i in range(1, z+1):
    if(z % i == 0):
        print(i)

# 3

def is_triangle(a, b, c):
    n = (b - c)
    if n < 0 :
        n = -n
    if n < a and a < b + c:
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


first = int(input("For Prime Numbers, Enter an integer to start from:\n"))
last = int(input("Enter an  integer to end:\n"))

def is_prime(number):
    isPrimeBool = True
    if number < 2:
        isPrimeBool = False  # because no number less than 2 is prime
    else:
        for j in range(2, number):
            if number % j == 0:
                isPrimeBool = False   #the number is divisable by any number lass than itself,then it is not prime.
    return isPrimeBool

for i in range(first,last + 1):
    if is_prime(i):
        print(i)

def fact(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


x = int(input("For the last part, Enter the number of people you have (the value of x):\n"))
y = int(input("Enter the number of people you want to pick and seat them around a table:\n"))

answer = (fact(x)/(fact(x - y) * fact(y))) * fact(y - 1)
print(answer)
