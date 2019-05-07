# class
# list (arrays)
# list("Hello")
# slicing (mylist[startpoint : endpoint])
# membership ( ... in ... operator returning true or false)
# len
# [1,2,3] + [4] = [1,2,3,4]
# 1 in [1,2,3] --> True
# [1,2,3] < [1,2] --> False . cuz anything is greater than NULL element
# indexing is 0 ..... 3
# 4 .... -1
# pay attention to return data type pf myList[:3] which is slicing which is a list
# access a list inside a list list[][]
# len([1, [1,2], 3]) --> 3
# min(lst) , max(lst), sum(lst)
# lists are mutable . for lists you can but for strings but you can't assign char directily, make a new string by "string.replace('a','z') this will replace every a with z"
# methods like : .append(5) adds the element as it is.   .extend([5]) grow the lists at the end of it. but extend needs to add a list containing the digits we want
# .pop()
# if you pop from an empty list, error: IndexError
# .insert(index,number) ...   .insert(3,20)
# if you insert after the last element, even if like .insert(50, 99) it will just add at the end of the list
# .remove(5) , removes the first number 5 in the last
# .sort() .reverse()
# random.shuffle(a)
# you can't assign those to something, cuz they dont return anything to the screen!

# for strings ::  "this is a test".split() .. by default ignores the spaces
# so .split() turns a string to a list that we can change
# ' '.join(list) join with space seperator and creates a string
# create a distinct copy by list[:]
