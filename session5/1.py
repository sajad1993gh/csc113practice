# int("40.5") --> Value error in python
# int(float("40.5"))
# only False and 0 are considered as False by python everything else is True
# ord("0") the order in the table
# chr(65)  --> 'A'
# if <condition>:
#      <statement>
# else:
#      <statement>

#if <condition1>:
#elif <condition2>:

#else:

#try:
#except:

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError as x:
        if str(x) == "math domain":
            print("divded by zero!")
        else:
            print("invalid")
    else:
        print(result)
    finally:
        print("finally")

divide(1,0)

def divide2(x,y):
    print(x/y)

divide2(1,0)
