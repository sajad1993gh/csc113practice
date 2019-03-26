
def collatz(n):
    try:
        n = int(n)
    except ValueError:
        print("Try to type a valid integer!")
    else:
        if n < 0:
            print("It was a negative integer, try to enter a positive integer!")
        elif n < 2:
            print("Try to enter an integer greater than 1. It should be at least 2!")
        else:
            if n % 2 ==0:
                newN = n//2
                print(newN)
                if newN != 1:
                    collatz(newN)
                else:
                    return (newN)
            elif n % 2 != 0:
                newN = 3 * n + 1
                print (newN)
                collatz(newN)

n = input("Enter an integer which is greater than 1 and not equal to 1 ( > 1)? \n")
collatz(n);

try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    print(a/b)
except ValueError:
    print("Please enter valid integers")
except ZeroDivisionError:
    print("The second number you entered was Zero, a number cannot be divided by Zero,\nplease try to enter a non zero number for that. ")
except:
    print("\nSomething went wrong, sorry!")


def primeFactors(n):
    if n<2:
        print("it doesnt have any prime factors")
    if n % 2 == 0:
        print(2)
    if n % 3 == 0:
        print(3)
    if n % 5 == 0:
        print(5)
    if n % 7 == 0:
        print(7)
    if n % 11 == 0:
        print(11)
    if n % 13 == 0:
        print(13)
    if n % 17 == 0:
        print(17)

n = int(input("Enter an integer to get its prime factors? \n"))
primeFactors(n)


def pFact(x):
    if x < 4:
        return;
    if x % 2 == 0:
        x = x - 1
        print(x)
        pFact(n)
    else:
        x = x - 2
        print(x)
        pFact(x)

x = int(input("Enter an integer to get the prime factors which are less than or equal to it? \n"))
pFact(x)
print(2);
