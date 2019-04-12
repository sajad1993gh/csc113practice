import random
# dir(random)
# random()
# uniform(min,max) Return a random floating point number N such that min <= N <= max
# randint(min,max) Return a random integer N such that min <= N <= max. Alias for randrange(min, max+1)
# randrange(min,max,step) modulo is optional. Return a randomly selected element from range(start, stop, step). This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
# shuffle(list) Shuffle the sequence
# sample[list,4] Return a k length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement. Returns a new list containing elements from the population while leaving the original population unchanged. 
# choice(list) returns one element randomly
# list [1,"a", 3 , ...]
# Tuple(1, "a", 3) unchangable
a = random.randrange(4,10,2)
print(a)
