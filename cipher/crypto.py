from functions import rotate


def encrypt(nessage, key):
    encrypted = ''
    for character in message:
        encrypted += rotate(character, key)
    return encrypted
