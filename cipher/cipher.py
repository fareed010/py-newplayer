# A simple cipher function
letter = input("Word: ")
key = int(input("Key: "))


def rotate(l, k):
    encrypted = ''
    for char in l:
        encrypted += ord(char) + k
    return encrypted


encrypt = rotate(letter, key)
print(encrypt)
