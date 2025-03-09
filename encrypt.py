import random
import string

# Encryption setup
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

# List to store encrypted texts
encrypted_texts = []

def encrypt_text(plain_text):
    cypher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cypher_text += key[index]
    return cypher_text

def decrypt_text(cypher_text):
    plain_text = ""
    for letter in cypher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text
