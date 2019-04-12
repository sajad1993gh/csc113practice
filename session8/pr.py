sentence = input("Enter your sentence to be encrypted>>  ")
encrypted = ""

for i in sentence:
    temp = ord(i) + 2
    encrypted += chr(temp)

print(encrypted)
