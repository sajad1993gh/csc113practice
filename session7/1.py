import random
# dir(random)
# random()
# uniform(min,max)
# randint(min,max)
# randrange(min,max,modulo) modulo is optional
# shuffle(list)
# sample[list,4]
# choice(list) returns one element randomly
# list [1,"a", 3 , ...]
# Tuple[1, "a", 3] unchangable
a = random.randrange(4,10,3)
print(a)

# for <var> in <sequence>:
#    <body>

for i in [0,1,2,3]:
    print(i)

for odd in [1,3,5,7]:
    print(odd*odd)

for i in range(100): # means range(0,100) or 0 to 99. range(start,finish) finish is excluded and start is included
    print(i)

type(range(100)) # it is range

for i in range(0,21,2): # 2 is the range step
    print(i)
# to go backward range(20,-1,-2) . you can't use float for none of them
