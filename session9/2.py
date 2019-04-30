""" file.read for reading from a file
"""

phonebook = open("phonebook.txt", "r")

#print(phonebook.read())


""" doing another time, it reads from the last point on """

#print(phonebook.read())

"""
print(phonebook.readline())
print(phonebook.readline())
print(phonebook.readline())

print(phonebook.readline())  this prints empty string
"""

#print(phonebook.readlines())

"""
phonebook.seek(0) sets the tracker at 0'th character
to read that do phonebook.readline()
phonebook.tell() tells you where your tracker is
"""
#making changes in the files:
with open("phonebook.txt", "a") as f:
    f.write("\nSajad: 3456789")
"""
what is you wanna add stuff to the beginning of the file without changing the stuff in it:

with open("phonebook.txt", "r+") as f:
    data1 = f.read() # saving it in data1
    f.seek(0)
    f.write("\nSajad: 3456789" + data1) # overwriting it

"""
"""
A = "king\'s"
"""
