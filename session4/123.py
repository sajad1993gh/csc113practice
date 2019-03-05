# SAJAD_GHOLAMZADEHRIZI
# SESSION AFTERNOON 1 _ InclassAssignment2
import math

def milliseconds(minutes):
    millisec= minutes*60000
    print (millisec)
    return
minutes=int(input("Enter time in minutes  "))
milliseconds(minutes)

def average(test1,test2):
    return (test1+test2)/2

firsttest = float(input("Enter the first test grades?  "))
secondtest = float(input("Enter the second test grades?  "))
print(average(firsttest,secondtest))

def roots():
    print("turn your equation into this form: ax**2 + bx + c = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    delta = (b**2) - (4*a*c)
    root1 = (-b - math.sqrt(delta))/(2*a)
    root2 = (-b + math.sqrt(delta))/(2*a)
    print(root1,root2)
    return

roots()

def conversion(temperature,unit):
    if (unit=='K'):
        return temperature * 1.25 + 273.15
    if (unit=='R'):
        return (temperature - 273.15) * 0.8
temp = float(input("Enter your temperature?  "))
unit = input("Enter your unit in capital letters as K or R?  ")
print(conversion(temp,unit))

#E:
def cube(n):
    cube_volume = n**3
    marble_volume = 4.0/3.0 * (math.pi) * ((n/4.0)**3)
    return cube_volume/marble_volume

numb = float(print("Enter the radius of cube?  ")
print(cube(numb))

