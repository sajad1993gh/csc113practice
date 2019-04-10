# extract the digit from a number

def digit_extraction(number,position):
    return (number//(10**position))%10


print(digit_extraction(123456,3));

def f():
    global a
    a = 1
    print(a)
a = 0
f()
print(a)

"""
def f2():
    return f2()

f2()
"""
