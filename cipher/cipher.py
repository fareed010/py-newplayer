# A simple cipher function
letter = input("Word: ")
key = input("Key: ")


def rotate(l, k):
    new = ord(letter) + key
    new = chr(new)
    return new


encrypt = rotate(letter, key)
print(encrypt)
