# extract the digit from a number

def digit_extraction(number,position):
    return number//(10**position)%10


print(digit_extraction(123456,4));
