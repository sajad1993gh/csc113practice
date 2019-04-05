# SAJAD_GHOLAMZADEHRIZI
# SESSION AFTERNOON 1 _ Assignment 4

import math
# 1

def perf_int(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if sum == n:
        return True;
    else:
        return False;

try:
    x = int(input("Enter an integer to check if it's perfect? \n"))
    n = perf_int(x)
    if str(n) == "True":
        print("Yes it is perfect")
    else:
        print("No it's not perfect")
except ValueError:
    print("Please enter a valid integer")
except:
    print("\nSomething went wrong, sorry!")

# 2
moreInt = "yes"
while moreInt[0] == "y" or moreInt[0] == "Y":
    z = int(input("Enter a positive integer to get all positive integer divisors:\n"))
    print("The divisors are:")
    for i in range(1, z+1):
        if(z % i == 0):
            print(i)
    moreInt = str(input("Would you like to try one more time?(yes or no)\n"))

# 3

def get_vertex():
    x = float(input("    Please enter x: "))
    y = float(input("    Please enter y: "))
    return x,y

def get_triangle():
    print("Your First vertex")
    x1,y1 = get_vertex()
    print("Your Second vertex")
    x2,y2 = get_vertex()
    print("Your Third vertex")
    x3,y3 = get_vertex()
    return x1, y1, x2, y2, x3, y3

def is_triangle(a, b, c):
    n = (b - c)
    if n < 0 :
        n = -n
    if n < a and a < b + c:
        return True
    return False

try:
    moreTriangle = "yes"
    while moreTriangle[0] == "y" or moreTriangle[0] == "Y":
        print("To check to see if your points make a triangle, enter your vertices")
        x1, y1, x2, y2, x3, y3 = get_triangle()
        a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        b = math.sqrt((x3-x1)**2 + (y3-y1)**2)
        c = math.sqrt((x3-x2)**2 + (y3-y2)**2)

        if is_triangle(a, b, c):
            print("Yes they form a triangle")
        else:
            print("No they can't form a triangle")
        moreTriangle = str(input("Do you have more points to examine? (yes or no)\n"))
except ValueError:
    print("Please enter a valid integer")
except:
    print("\nSomething went wrong, sorry!")
# 4

def is_prime(number):
    isPrimeBool = True
    if number < 2:
        isPrimeBool = False  # because no number less than 2 is prime
    else:
        for j in range(2, number):
            if number % j == 0:
                isPrimeBool = False   #the number is divisable by any number lass than itself,then it is not prime.
    return isPrimeBool

moreNum = "yes"
while moreNum[0] == "y" or moreNum[0] == "Y":
    first = int(input("To get the Prime Numbers, Enter an integer to start from:\n"))
    last = int(input("Enter an  integer to end:\n"))
    for i in range(first,last + 1):
        if is_prime(i):
            print(i)
    moreNum = str(input("Do you want to try one more time? (yes or no) \n"))

# 5

def fact(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

morePeople = "yes"
while morePeople[0] == "y" or morePeople[0] == "Y":
    x = int(input("Enter the number of people you have (the value of X in the Assignment):\n"))
    y = int(input("Enter the number of people you want to pick and seat them around a table (the value of Y):\n"))
    answer = (fact(x)/(fact(x - y) * fact(y))) * fact(y - 1)
    print(answer)
    morePeople = str(input("Would you like to try one more time? (yes or no)\n"))
