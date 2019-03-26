try:
    n = int(input("How many?"))
    sum = 0.0
    for i in range(n):
        x = float(input("Enter number>> "))
        sum = sum + x
    print("\n", sum/n)
except:
    print("zero!!!")
