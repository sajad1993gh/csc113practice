# SAJAD_GHOLAMZADEHRIZI
# SESSION AFTERNOON 1 _ InclassAssignment2
import math

def milliseconds(minutes):
    millisec= minutes*60000
    print (millisec)

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

roots()

def kelvin_to_reamur(temp):
        return (temp - 273.15) * 0.8
def reamur_to_celsius(temp):
        reamur = kelvin_to_reamur(temp)
        return reamur * 1.25

temp = float(input("Enter your temperature in kelvin?  "))
print(reamur_to_celsius(temp))

def cube(n):
    cube_volume = n**3
    marble_volume = (2* (n/4))**3
    return cube_volume/marble_volume

number= float(input("Enter the radius of the cube?  "))
print("You can fit",cube(number),"marbles in the cube")



def graph1():
    print("^ - ^^ - ^^ - ^^ - ^^ - ^^ - ^^ - ^^ - ^")


def graph2():
    graph1()
    print("i         i         i         i        i")
    print("i         i         i         i        i")
    print("i         i         i         i        i")
    print("i         i         i         i        i")


graph2()
graph2()
graph2()
graph2()
graph1()
