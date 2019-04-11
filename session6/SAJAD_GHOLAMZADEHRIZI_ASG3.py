# SAJAD_GHOLAMZADEHRIZI
# SESSION AFTERNOON 1 _ InclassAssignment3
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
                #else:
                    #return (newN)
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


def is_prime(number):
    if(number == 1):
        return False
    for x in range(2,number):
        if number % x == 0:
            return False
    return True

def primeFactors(n, i):
    if(n == 1):
        return
    elif(n%i == 0):
        print(i)
        primeFactors(n//i, i)
    else:
        primeFactors(n, i+1)


n = int(input("Enter a number: "))
primeFactors(n,2)


def iss_prime(n, i=2):
    if i == n:
        return True
    else:
        return n % i != 0 and iss_prime(n, i + 1)


def print_primes(n):
    if n > 1:
        print_primes(n - 1)
        if iss_prime(n):
            print(n, end=' ')


n = int(input('Enter a value for n: '))
print('Primes numbers upto', n, 'are:', end=' ')
print_primes(n)
print()
