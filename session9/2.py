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

print(phonebook.readline()) # this prints empty string
""""

print(phonebook.readlines())
