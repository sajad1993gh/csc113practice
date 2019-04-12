import random
# dir(random)
# random()
# uniform(min,max) Return a random floating point number N such that min <= N <= max
# randint(min,max) Return a random integer N such that min <= N <= max. Alias for randrange(min, max+1)
# randrange(min,max,step) modulo is optional. Return a randomly selected element from range(start, stop, step). This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
# shuffle(list) Shuffle the sequence
# sample(list,k) Return a k length list of unique elements chosen from the list. Used for random sampling without replacement. Returns a new list containing elements from the list while leaving the original list unchanged.
# choice(list) Return a random element from the non-empty list
# list [1,"a", 3 , ...]
# Tuple(1, "a", 3) unchangable
a = random.randrange(4,10,2)
print(a)

# for <var> in <sequence>:
#    <body>

for i in [0,1,2,3]:
    print(i)

for odd in [1,3,5,7]:
    print(odd*odd)

for i in range(100): # means range(0,100) or 0 to 99. range(start,finish) finish is excluded and start is included
    print(i)

print(range(100))
print(type(range(100))) # it is range

for i in range(0,21,2): # 2 is the range step
    print(i)
# to go backward range(20,-1,-2) . you can't use float for none of them

for i in range(20, -1, -2):
    print(i)
