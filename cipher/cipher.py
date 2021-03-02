# A simple cipher function
letter = input("Word: ")
key = int(input("Key: "))


def rotate(l, k):
    new = ord(l) + k
    new = chr(new)
    return new


encrypt = rotate(letter, key)
print(encrypt)
