from functions import rotate


def encrypt(message, key):
    encrypted = ''
    for character in message:
        encrypted += rotate(character, key)
    return encrypted
